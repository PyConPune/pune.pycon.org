import account.views

from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from cauth.forms import SignupForm
from cauth.utils import generate_username
from root.utils import validate_year


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


def logout_view(request, year):
    """ This view logs out the user. """
    
    if not validate_year(year):
        raise Http404

    logout(request)
    return redirect('homepage')
