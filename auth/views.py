import account.views

from django.shortcuts import render
from django.views.generic import TemplateView

from auth.forms import SignupForm


class SignupView(account.views.SignupView):

    form_class = SignupForm
    identifier_field = 'email'
    template_name = 'account/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        username = "<magic>"
        return username
