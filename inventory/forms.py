from django import forms
from inventory.models import UserTshirt


class UserTshirtForm(forms.ModelForm):
    """ Ticket Application Form """

    class Meta:
        model = UserTshirt
        fields = [
            "tshirt"
        ]