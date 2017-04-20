from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login as user_login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

from transportation_management.models import Vehicle, TravelReport
from .forms import AuthenticationForm, TravelReportForm


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
            if user.is_staff:
                return HttpResponseRedirect('/list/')
            else:
                return HttpResponseRedirect('/create/')

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
@require_http_methods(['POST', 'GET'])
def create(request):
    vars = {}
    vars['vehicles'] = Vehicle.objects.all()
    form = TravelReportForm(request.POST or None)
    vars['form'] = form
    if form.is_valid():
        travel_report = form.save()
        print(travel_report)
        return HttpResponseRedirect(reverse('transportation_management:read', kwargs={'id': travel_report.id}))

    return render(request, 'transportation_management/create.html', vars)


@login_required
@require_http_methods(['GET'])
def read(request, id):
    vars = {}
    travel_report = get_object_or_404(TravelReport, pk=id)
    vars['travel_report'] = travel_report

    return render(request, 'transportation_management/read.html', vars)


@login_required
@require_http_methods(['GET'])
def list(request):
    vars = {}
    vars['travel_reports'] = TravelReport.objects.all()

    return render(request, 'transportation_management/list.html', vars)
