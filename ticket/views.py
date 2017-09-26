from random import choice
from string import ascii_lowercase, digits

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from cauth.models import UserProfile
from cauth.views import SignupView
from payments.razorpay.razorpay_payments import RazorpayPayments
from ticket.forms import UserRegistrationForm
from ticket.forms import TicketApplicationForm
from ticket.models import Ticket, UserTicket, AuxiliaryTicket
from payments.models import Invoice, RazorpayKeys
from inventory.models import Tshirt, UserTshirt


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

    @staticmethod
    def _get_auxiliary_tickets():
        tickets = AuxiliaryTicket.objects.values(
            'title',
            'price',
            'description',
            'image_base64_text',
            'image_base64_title',
        )

        return tickets

    @staticmethod
    def _get_tshirts():
        tshirts = Tshirt.objects.values(
            'id',
            'gender',
            'size',
            'price',
            'description',
            'image_base64_text',
            'image_base64_title',
        )

        return tshirts

    def _get_tshirts_from_ids(self, tshirt_ids):
        tshirts = []
        for id in tshirt_ids:
            if id != '':
                tshirt = Tshirt.objects.get(id=int(id))
                tshirts.append(tshirt)

        return tshirts

    def _generate_username(self, length=16, chars=ascii_lowercase+digits,
                           split=4, delimiter='-'):

        username = ''.join([choice(chars) for i in range(length)])
        if split:
            username = delimiter.join([
                username[start:start+split]
                for start in range(0, len(username), split)])

        return username

    def _generate_payable_amount(self, user_ticket, user_tshirts):
        ticket = user_ticket.ticket
        auxiliary_ticket_ids = user_ticket.auxiliary_ticket_id.split(",")
        auxiliary_tickets = []
        if int(auxiliary_ticket_ids[0]) != 0:
            auxiliary_tickets = [
                AuxiliaryTicket.objects.get(id=int(x)) for x in auxiliary_ticket_ids
            ]

        payable_amount = ticket.price

        for auxiliary_ticket in auxiliary_tickets:
            payable_amount = payable_amount + auxiliary_ticket.price

        for user_tshirt in user_tshirts:
            payable_amount = payable_amount + user_tshirt.tshirt.price

        return payable_amount

    def _generate_invoice_amount(self, amount):
        return (amount + amount * 0.18) * 100

    def _generate_invoice_description(self, forms):
        raise NotImplementedError

    def _get_keys(self):
        return RazorpayKeys.objects.first()

    def _initiate_payment(self, user, profile, title, description, amount):
        keys = self._get_keys()
        payment = RazorpayPayments(keys.api_key, keys.api_secret)
        fullname = '{} {}'.format(profile.first_name, profile.last_name)
        customer = {
            "email": user.email,
            "contact": profile.contact,
            "name": fullname
        }

        items = [{
            "name": title,
            'description': description,
            "amount": amount,
            "currency": "INR"
        }]

        invoice = payment.create_invoice(customer=customer, items=items)

        return invoice

    def _validate_request_pre_save(self, ticket, auxiliary_ticket_ids):
        user_ticket_count = UserTicket.objects.filter(ticket=ticket).count()
        for id in auxiliary_ticket_ids.split(","):
            if int(id) != 0:
                auxiliary_ticket = AuxiliaryTicket.objects.get(id=int(id))
                auxiliary_ticket_count = UserTicket.objects.filter(
                    auxiliary_ticket_id__contains=id
                ).count()
                if auxiliary_ticket_count >= auxiliary_ticket.limit:
                    return False
        if user_ticket_count < ticket.limit:
            return True
        else:
            ticket.is_limit_reached = True
            ticket.save()
            return False

    def get(self, request, *args, **kwargs):
        ticket_form = self.ticket_form_cls()
        user_form = self.user_form_cls()
        tickets = self._get_tickets()
        auxiliary_tickets = self._get_auxiliary_tickets()
        tshirts = self._get_tshirts()

        return render(
            request, self.template_name, {
                'ticket_form': ticket_form,
                'user_form': user_form,
                'tickets': tickets,
                'auxiliary_tickets': auxiliary_tickets,
                'tshirts': tshirts,
            }
        )

    def post(self, request, *args, **kwargs):
        ticket_form = self.ticket_form_cls(request.POST)
        user_form = self.user_form_cls(request.POST)
        tshirt_ids = request.POST.getlist('tshirts[]')

        tickets = self._get_tickets()
        auxiliary_tickets = self._get_auxiliary_tickets()
        tshirts = self._get_tshirts()

        is_ticket_form_valid = ticket_form.is_valid()
        is_user_form_valid = user_form.is_valid()

        if 'ticket' not in ticket_form.cleaned_data:
            return render(
                request, self.template_name, {
                    'ticket_form': ticket_form,
                    'user_form': user_form,
                    'tickets': tickets,
                    'auxiliary_tickets': auxiliary_tickets,
                    'tshirts': tshirts,
                }
            )

        ticket = ticket_form.cleaned_data['ticket']
        auxiliary_ticket_id = ticket_form.cleaned_data['auxiliary_ticket_id']
        selected_tshirts = self._get_tshirts_from_ids(tshirt_ids)

        is_ticket_left = self._validate_request_pre_save(
                        ticket,
                        auxiliary_ticket_id)

        if is_ticket_form_valid and is_user_form_valid and is_ticket_left:
            user = self.create_user(user_form)
            profile = self.create_profile(user_form, user=user)

            user_tshirts = self.save_user_tshirts(selected_tshirts, user)

            user_ticket = ticket_form.save(commit=False)
            user_ticket.user = user
            user_ticket.auxiliary_ticket_id = auxiliary_ticket_id
            user_ticket.save()

            amount = self._generate_payable_amount(
                    user_ticket=user_ticket,
                    user_tshirts=user_tshirts,
                )
            amount = self._generate_invoice_amount(
                    amount)
            # description = self._generate_invoice_description(
            #        forms=[user_ticket])
            invoice = self._initiate_payment(
                user=user, profile=profile, title='PyCon Pune 2018',
                description="", amount=amount)

            self.save_invoice_data(invoice, user, user_ticket, user_tshirts)

            return HttpResponseRedirect(invoice['short_url'])

        return render(
            request, self.template_name, {
                'ticket_form': ticket_form,
                'user_form': user_form,
                'tickets': tickets,
                'auxiliary_tickets': auxiliary_tickets,
                'tshirts': tshirts,
            }
        )

    def create_user(self, form, **kwargs):
        User = get_user_model()

        user = User(**kwargs)
        username = self._generate_username()
        while True:
            try:
                User.objects.get(username=username)
                username = self._generate_username()
            except User.DoesNotExist:
                break
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

    def save_user_tshirts(self, tshirts, user):

        user_tshirts = []
        for tshirt in tshirts:
            user_tshirt = UserTshirt(tshirt=tshirt, user=user)
            user_tshirt.save()
            user_tshirts.append(user_tshirt)

        return user_tshirts

    def save_invoice_data(self, payment_invoice, user, user_ticket,
                          user_tshirts, conference=1):
        """ Saves data for the invoice created using razorpay """

        invoice = Invoice(user=user.id, conference=conference)
        invoice.invoice_id = payment_invoice['id']
        invoice.receipt_number = payment_invoice['receipt']
        invoice.order_id = payment_invoice['order_id']
        invoice.payment_id = payment_invoice['payment_id']
        invoice.status = payment_invoice['status']
        invoice.expire_by = payment_invoice['expire_by']
        invoice.issued_at = payment_invoice['issued_at']
        invoice.paid_at = payment_invoice['paid_at']
        invoice.amount = payment_invoice['amount']
        invoice.currency = payment_invoice['currency']
        invoice.short_url = payment_invoice['short_url']
        invoice.save()

        user_ticket.invoice = payment_invoice['id']
        user_ticket.save()

        for user_tshirt in user_tshirts:
            user_tshirt.invoice = payment_invoice['id']
            user_tshirt.save()

def acknowledge(request):
    return render(request, 'ticket/thanks.html')


def registration(request):
    """ This is the first version of the JS based razorpay checkout page """
    return render(request, "ticket/ticketv0.html")
