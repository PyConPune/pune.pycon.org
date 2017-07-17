from django import forms
from django.utils.translation import ugettext as _

from ticket.models import Ticket, UserTicket


class TicketApplicationForm(forms.ModelForm):
    """ Ticket Application Form """

    class Meta:
        model = UserTicket
        fields = [
            "ticket",
        ]
