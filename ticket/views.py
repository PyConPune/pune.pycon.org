from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from cauth.models import UserProfile
from cauth.views import SignupView
from payments.razorpay.payments import RazorpayPayments
from ticket.forms import UserRegistrationForm
from ticket.forms import TicketApplicationForm
from ticket.models import Ticket, UserTicket


class TicketApplicationView(TemplateView):

    ticket_form_cls = TicketApplicationForm
    user_form_cls = UserRegistrationForm
    template_name = 'ticket/application.html'

    @staticmethod
    def _get_tickets():
        tickets = Ticket.objects.values(
            'title',
            'price',
            'description',
            'image_base64_text',
            'image_base64_title',
        )

        return tickets

    def _generate_payable_amount(self, forms):
        raise NotImplementedError

    def _generate_invoice_amount(self, amount):
        return (amount + amount * 0.18) * 100

    def _generate_invoice_description(self, forms):
        raise NotImplementedError

    def _initiate_payment(user, profile, title, description, amount):
        payment = RazorpayPayments()
        customer = {
            "email": user.email,
            "contact": profile.contact
        }

        items = [{
            "name": title,
            'description': description,
            "amount": amount,
            "currency": "INR"
        }]
            
        invoice = payment.createInvoice(customer=customer, items=items)

        return invoice

    def get(self, request, *args, **kwargs):
        ticket_form = self.ticket_form_cls()
        user_form = self.user_form_cls()
        tickets = self._get_tickets()

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
        tickets = self._get_tickets()

        if ticket_form.is_valid() and user_form.is_valid():
            user_ticket = ticket_form.save()
            user = self.create_user(user_form, model=get_user_model())
            profile = self.create_profile(user_form, user=user)

            amount = self._generate_payable_amount(
                    forms=[user_ticket])
            amount = self._generate_invoice_amount(
                    amount)
            description = self._generate_invoice_description(
                    forms=[user_ticket])
            payment, invoice = self._initiate_payment(
                    user=user, profile=profile, title='PyCon Pune 2018',
                    description=description)
            
            return HttpResponseRedirect(invoice['short_url'])

        return render(
            request, self.template_name, {
                'ticket_form': ticket_form,
                'user_form': user_form,
                'tickets': tickets
            }
        )

    def create_user(self, form, model=None, **kwargs):
        if model is None:
            User = get_user_model()
        
        user = User(**kwargs)
        username = self._generate_username(form)
        user.username = username
        user.email = form.cleaned_data['email']
        user.set_unusable_password()
        user.save()

        return user

    def create_profile(self, form, user, **kwargs):

        profile = UserProfile(user=user)
        profile.first_name = form.cleaned_data['first_name']
        profile.last_name = form.cleaned_data.get('last_name')
        profile.contact = form.cleaned_data['contact']
        profile.location = form.cleaned_data.get('location')
        profile.gender = form.cleaned_data.get('gender')
        profile.company = form.cleaned_data.get('company')
        profile.job_title = form.cleaned_data.get('job_title')
        
        age_group = form.cleaned_data.get('age_group')
        if age_group == '0':
            age_group = None
        profile.age_group = age_group

        job_title = form.cleaned_data.get('job_title')
        if job_title == 'Z':
            job_title = None
        profile.job_title = job_title

        profile.save()

        return profile


def acknowledge(request):
    return render(request, 'ticket/thanks.html')


def registration(request):
    """ This is the first version of the JS based razorpay checkout page """
    return render(request, "ticket/ticketv0.html")
