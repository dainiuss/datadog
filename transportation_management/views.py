from django.shortcuts import render
from django.contrib.auth import login as user_login
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .forms import AuthenticationForm


@never_cache
@require_http_methods(["GET", "POST"])
def authenticate(request):

    vars = {}
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm(request.POST or None)
        vars['form'] = form
        if form.is_valid():
            user = form.get_user()
            user_login(request, user)
            return HttpResponseRedirect('/')

    return render(request, 'transportation_management/login.html', vars)


@require_http_methods(['GET'])
def login(request):
    vars = {}

    return render(request, 'transportation_management/login.html', vars)

@login_required
@require_http_methods(['GET'])
def index(request):
    vars = {}

    return render(request, 'transportation_management/index.html', vars)

@login_required
@require_http_methods(['GET'])
def list(request):
    vars = {}

    return render(request, 'transportation_management/list.html', vars)