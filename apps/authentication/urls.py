from django.urls import path, include

from django.urls import path
from django.conf import settings
from .views import home

app_name = 'authentication'


urlpatterns = [
    path("", home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
]
