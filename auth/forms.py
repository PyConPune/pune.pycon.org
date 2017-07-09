import account.forms


class SignupForm(account.forms.SignupForm):
    """ Signup Form """

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
