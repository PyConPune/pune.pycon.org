from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from cauth.views import SignupView
from payments.razorpay.payments import RazorpayPayments
from ticket.forms import UserRegistrationForm
from ticket.forms import TicketApplicationForm
from ticket.models import Ticket, UserTicket


class TicketApplicationView(TemplateView):

    ticket_form_cls = TicketApplicationForm
    user_form_cls = UserRegistrationForm
    template_name = 'ticket/application.html'

    def get(self, request, *args, **kwargs):

        year = kwargs.get('year')

        ticket_form = self.ticket_form_cls()
        user_form = self.user_form_cls()
        tickets = Ticket.objects.all(year=year)

        return render(
            request, self.template_name, {
                'ticket_form': ticket_form,
                'user_form': user_form,
                'tickets': tickets
            }
        )

    def post(self, request, *args, **kwargs):
        ticket_form = self.ticket_form_cls(request.POST)
        user_form = self.user_form_cls(request.POST)
        tickets = Ticket.objects.all()

        if ticket_form.is_valid() and user_form.is_valid():
            ticket = ticket_form.cleaned_data['ticket']
            user_ticket_count = UserTicket.objects.filter(ticket=ticket).count()
            if user_ticket_count < ticket.limit:
                payment = RazorpayPayments()
                customer = {
                    "email": user_form.cleaned_data['email'],
                    "contact": user_form.cleaned_data['contact']
                }
                items = [{
                    "name": ticket_form.cleaned_data['ticket'].title,
                    "amount": ticket_form.cleaned_data['ticket'].price * 100,
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


def acknowledge(request, year):
    return render(request, 'ticket/thanks.html')


def registration(request, year):
    """ This is the first version of the JS based razorpay checkout page """
    return render (request, "ticket/ticketv0.html")
