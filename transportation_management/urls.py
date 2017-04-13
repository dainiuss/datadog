from django.conf.urls import url
from .views import index, login, authenticate, list
from django.contrib.auth.views import logout


app_name = 'transportation_management'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^list/', list, name='list'),
    url(r'^authenticate/', authenticate, name='authenticate'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, kwargs={"next_page": "/login"}, name="logout"),
]