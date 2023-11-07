from django.urls import path

from basketapp.apps import BasketappConfig
from basketapp.views import basket, basket_add, basket_remove, basket_edit

app_name = BasketappConfig.name

urlpatterns = [
    path('', basket, name='basket'),
    path('add/<int:pk>/', basket_add, name='add'),
    path('remove/<int:pk>/', basket_remove, name='remove'),
    path('edit/<int:pk>/<int:nights>/', basket_edit, name='edit'),
]
