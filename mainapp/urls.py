from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import main, accommodation, accommodations

app_name = MainappConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('accommodation_details/<int:pk>', accommodation, name='accommodation'),
    path('accommodations/', accommodations, name='accommodations')
]
