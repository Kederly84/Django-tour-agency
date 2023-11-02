from django.urls import path

from adminapp.apps import AdminappConfig
from adminapp.views import (
    TravelUserListView,
    user_create,
    user_update,
    user_delete,
    countries,
    CountryCreateView,
    CountryUpdateView,
    CountryDeleteView,
    accommodations,
    accommodation_create,
    accommodation_delete,
    accommodation_update,
    AccommodationDetailView
)

app_name = AdminappConfig.name

urlpatterns = [
    path('', TravelUserListView.as_view(), name='users'),
    path('users/edit/<int:pk>/', user_update, name='user_update'),
    path('users/create/', user_create, name='user_create'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),
    # CRUD realization
    path('countries/', countries, name='countries'),
    path('countries/create/', CountryCreateView.as_view(), name='country_create'),
    path('countries/update/<int:pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('countries/delete/<int:pk>/', CountryDeleteView.as_view(), name='country_delete'),

    path('accommodations/read/countries/<int:pk>/', accommodations, name='accommodations'),
    path('accommodations/create/countries/<int:pk>/', accommodation_create, name='accommodation_create'),
    path('accommodations/delete/<int:pk>/', accommodation_delete, name='accommodation_delete'),
    path('accommodations/update/<int:pk>/', accommodation_update, name='accommodation_update'),
    path('accommodations/read/<int:pk>/', AccommodationDetailView.as_view(), name='accommodation_read'),
]
