import datetime
from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _

from transportation_management.models import TravelReport


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

    username = forms.CharField(max_length=254, error_messages={"required": default_error_messages["required_username"],
                                                               "invalid": default_error_messages["invalid_username"]})
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(),
                               error_messages={"required": default_error_messages["required_password"]})

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


class TravelReportForm(forms.ModelForm):
    class Meta:
        model = TravelReport
        fields = ['vehicle', 'route', 'date', 'time_left_terminal', 'time_arrived_to_client',
                  'time_left_client', 'time_back_to_terminal', 'time_unloading',
                  'speedometer_at_leaving', 'speedometer_at_arrival']

        error_messages = {
            'vehicle': {
                "required": _('Vehicle is required.'),
                "invalid": _('Vehicle is invalid.'),
            },
            'route': {
                "required": _('Route is required.'),
                "invalid": _('Route is invalid.')
            },
            'date': {
                "required": _('Date is required.'),
                "invalid": _('Date is invalid.')
            },
            'time_left_terminal': {
                "required": _('Time left terminal is required.'),
                "invalid": _('Time left terminal is invalid.')
            },
            'time_arrived_to_client': {
                "required": _('Time arrived to client is required.'),
                "invalid": _('Time arrived to client is invalid.')
            },
            'time_left_client': {
                "required": _('Time left the client is required.'),
                "invalid": _('Time left the client is invalid.')
            },
            'time_back_to_terminal': {
                "required": _('Time back to the terminal is required.'),
                "invalid": _('Time back to the terminal is invalid.')
            },
            'time_unloading': {
                "required": _('Unloading time is required.'),
                "invalid": _('Unloading time is invalid.')
            },
            'speedometer_at_leaving': {
                "required": _('Speedometer at leaving is required.'),
                "invalid": _('Speedometer at leaving is invalid.')
            },
            'speedometer_at_arrival': {
                "required": _('Speedometer at arrival is required.'),
                "invalid": _('Speedometer at arrival is invalid.')
            },
        }

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        self.initial = self.get_initial()
        super(TravelReportForm, self).__init__(initial=self.initial, instance=self.instance, *args, **kwargs)

    def get_initial(self):
        initial = {'vehicle': '',
                   'route': '',
                   'date': datetime.datetime.now().date().strftime("%m/%d/%Y"),
                   'time_left_terminal': '',
                   'time_arrived_to_client': '',
                   'time_left_client': '',
                   'time_back_to_terminal': '',
                   'time_unloading': '',
                   'speedometer_at_leaving': '',
                   'speedometer_at_arrival': ''}
        return initial
