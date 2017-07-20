from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from ticket.models import Ticket, UserTicket
from ticket.forms import TicketApplicationForm
from auth.forms import UserRegistrationForm

from auth.views import SignupView

from payments.razorpay.payments import RazorpayPayments


class TicketApplicationView(TemplateView):

    form_ticket = TicketApplicationForm
    form_user = UserRegistrationForm
    template_name = 'ticket/application.html'

    def get(self, request, *args, **kwargs):
        form1 = self.form_ticket()
        form2 = self.form_user()
        tickets = Ticket.objects.all()
        return render(request, self.template_name,
                      {'form_ticket': form1,
                       'form_user': form2,
                       'tickets': tickets})

    def post(self, request, *args, **kwargs):
        form1 = self.form_ticket(request.POST)
        form2 = self.form_user(request.POST)
        tickets = Ticket.objects.all()

        if form2.is_valid() and form1.is_valid():
            ticket = form1.cleaned_data['ticket']
            userticketcount = UserTicket.objects.filter(ticket=ticket).count()
            if userticketcount < ticket.limit:
                payment = RazorpayPayments()
                customer = {
                    "email": form2.cleaned_data['email'],
                    "contact": form2.cleaned_data['contact']
                }
                items = [{
                    "name": form1.cleaned_data['ticket'].title,
                    "amount": form1.cleaned_data['ticket'].price * 100,
                    "currency": "INR"
                }]
                invoice = payment.createInvoice(customer=customer, items=items)
                short_url = invoice['short_url']
                signup = SignupView()
                signup.generate_username(form2)
                user = signup.create_user(form2)
                userticket = UserTicket(user=user, ticket=ticket)
                userticket.save()
                return HttpResponseRedirect(short_url)
        return render(request, self.template_name,
                      {'form_ticket': form1,
                       'form_user': form2,
                       'tickets': tickets})


def thanks(request):
    return render(request, 'ticket/thanks.html')


def registration(request):
    """ This is the first version of the JS based razorpay checkout page """
    return render (request, "ticket/ticketv0.html")