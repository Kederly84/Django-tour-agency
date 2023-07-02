from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import main

app_name = MainappConfig.name

urlpatterns = [
    path('', main),
]
