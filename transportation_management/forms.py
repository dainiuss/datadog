from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _


class AuthenticationForm(forms.Form):

    default_error_messages = {
        'invalid_username': _('Username is invalid.'),
        "required_username": _("Username is required."),
        "required_password": _("Password is required."),
    }

    error_messages = {
        'invalid_login': _("Username and/or password is invalid."),
        'inactive': _("This account is inactive."),
    }

    username = forms.CharField(max_length=254, error_messages={"required": default_error_messages["required_username"], "invalid": default_error_messages["invalid_username"]})
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(), error_messages={"required": default_error_messages["required_password"]})

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(self.error_messages['invalid_login'])
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
