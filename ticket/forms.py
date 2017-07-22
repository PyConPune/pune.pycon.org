from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

import account.forms

from cauth.models import AGE_GROUP_CHOICES, OCCUPATION_CHOICES
from ticket.models import UserTicket


class TicketApplicationForm(forms.ModelForm):
    """ Ticket Application Form """

    class Meta:
        model = UserTicket
        fields = [
            "ticket",
        ]

    def clean(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        cleaned_data = self.cleaned_data
        ticket = cleaned_data['ticket']

        user_ticket_count = UserTicket.objects.filter(ticket=ticket).count()
        if user_ticket_count < ticket.limit:
            super(TicketApplicationForm, self).save(*args, **kwargs)
        else:
            self.ticket.is_limit_reached = True
            self.ticket.save()


class UserRegistrationForm(account.forms.SignupForm):
    
    first_name = forms.CharField(
        label=_('First Name'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('First Name')
        }
    ))
    last_name = forms.CharField(
        label=_('Last Name'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Last Name')
        }),
        required=False,
    )
    contact = forms.CharField(
        label=_('Contact'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Contact')
        }
    ))
    location = forms.CharField(
        label=_('Location'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Location')
        }),
        required=False,
    )
    age_group = forms.TypedChoiceField(
        label=_('Age Group'),
        choices=AGE_GROUP_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        required=False,
    )
    gender = forms.CharField(
        label=_('Gender'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Gender')
        }),
        required=False,
    )
    occupation = forms.TypedChoiceField(
        label=_('Occupation'),
        choices=OCCUPATION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': _('Occupation'),
        }),
    )
    company = forms.CharField(
        label=_('Company'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Company')
        }),
        required=False,
    )
    job_title = forms.CharField(
        label=_('Job Title'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Job Title'),
        }),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
        del self.fields["password"]
        del self.fields["password_confirm"]

        self.fields.keyOrder = [
            "email",
            "first_name",
            "last_name",
            "contact",
            "location",
            "age_group",
            "gender",
            "occupation",
            "company",
            "company_title",
            "website"
        ]
 
        self.fields['email'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Email')
        })
        self.fields['email'].required = True

        AGE_GROUP_CHOICES.insert(0, ('0', _('Please select an age group.')))
        self.fields['age_group'].choices = AGE_GROUP_CHOICES

        OCCUPATION_CHOICES.insert(0, ('Z', _('Please select an occupation.')))
        self.fields['occupation'].choices = OCCUPATION_CHOICES
