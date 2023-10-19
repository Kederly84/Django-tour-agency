from django.urls import path
from authapp.apps import AuthappConfig
from authapp.views import register, logout, login, edit


app_name = AuthappConfig.name

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('', login, name='login'),
    path('edit/', edit, name='edit')
]

