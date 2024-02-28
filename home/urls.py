from django.urls import path

from home.views import home
from home.apps import HomeConfig


app_name = HomeConfig.name

urlpatterns = [
    path('', home, name='home'),
]
