import account.forms

from django import forms
from auth.models import UserProfile


class SignupForm(account.forms.SignupForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email_confirm = forms.EmailField(label="Confirm Email")

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
        self.fields.keyOrder = [
            "email",
            "email_confirm",
            "first_name",
            "last_name",
            "password",
            "password_confirm"
        ]

    def clean_email_confirm(self):
        email = self.cleaned_data.get("email")
        email_confirm = self.cleaned_data["email_confirm"]
        if email:
            if email != email_confirm:
                raise forms.ValidationError("Email address must match previously typed email address")
        return email_confirm


class UserRegistrationForm(account.forms.SignupForm):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    age_group = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    company_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    website = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control'}))

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