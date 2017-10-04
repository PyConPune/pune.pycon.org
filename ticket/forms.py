from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

import account.forms

from cauth.models import AGE_GROUP_CHOICES, OCCUPATION_CHOICES, TSHIRT_SIZE_CHOICES
from ticket.models import UserTicket


class TicketApplicationForm(forms.ModelForm):
    """ Ticket Application Form """

    class Meta:
        model = UserTicket
        fields = [
            "ticket",
            "auxiliary_ticket_id"
        ]


class UserRegistrationForm(account.forms.SignupForm):
    first_name = forms.CharField(
        label=_('First Name'),
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('First Name')
        },
    ))
    last_name = forms.CharField(
        label=_('Last Name'),
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Last Name')
        }),
    )
    contact = forms.CharField(
        label=_('Contact No.'),
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Contact')
        },
    ))
    location = forms.CharField(
        label=_('Location'),
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Location')
        }),
    )
    age_group = forms.TypedChoiceField(
        label=_('Age Group'),
        required=True,
        choices=AGE_GROUP_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
    )
    gender = forms.CharField(
        label=_('Gender'),
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Gender')
        }),
    )
    tshirt_size = forms.TypedChoiceField(
        label=_('Tshirt Size'),
        required=True,
        choices=TSHIRT_SIZE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
    )
    occupation = forms.TypedChoiceField(
        label=_('Occupation'),
        required=True,
        choices=OCCUPATION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': _('Occupation'),
        }),
    )
    company = forms.CharField(
        label=_('Company'),
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Company')
        }),
    )
    job_title = forms.CharField(
        label=_('Job Title'),
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Job Title'),
        }),
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
            "tshirt_size",
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

        if AGE_GROUP_CHOICES[0][0] != '0':
            AGE_GROUP_CHOICES.insert(0, ('0', _('Please select an age group.')))
        self.fields['age_group'].choices = AGE_GROUP_CHOICES

        if OCCUPATION_CHOICES[0][0] != 'Z':
            OCCUPATION_CHOICES.insert(0, ('Z', _('Please select an occupation.')))
        self.fields['occupation'].choices = OCCUPATION_CHOICES

        if TSHIRT_SIZE_CHOICES[0][0] != 'XXX':
            TSHIRT_SIZE_CHOICES.insert(0, ('XXX', _('Please select a tshirt size.')))
        self.fields['tshirt_size'].choices = TSHIRT_SIZE_CHOICES
