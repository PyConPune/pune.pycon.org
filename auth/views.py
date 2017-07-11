import account.views

from django.shortcuts import render
from django.views.generic import TemplateView

from auth.forms import SignupForm
from auth.utils import generate_username


class SignupView(account.views.SignupView):

    form_class = SignupForm

    def create_user(self, form, commit=True):
        user_kwargs = {
            "first_name": form.cleaned_data["first_name"],
            "last_name": form.cleaned_data["last_name"]
        }
        return super(SignupView, self).create_user(form, commit=commit,
                                                   **user_kwargs)

    def generate_username(self, form):
        return generate_username(form.cleaned_data['email'])


class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm
