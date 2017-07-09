from django.forms import ModelForm
from django.contrib.auth.models import User

class UserSignupForm(ModelForm):
    class Meta:
        model = User
        fields =
