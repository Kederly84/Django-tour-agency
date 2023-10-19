from django.contrib import auth
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.forms import TravelUserRegistrationForm, TravelUserLoginForm, TravelUserEditForm, TravelUserProfileEditForm


# Create your views here.

def register(request):
    title = 'Registration'

    if request.method == 'POST':
        register_form = TravelUserRegistrationForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = TravelUserRegistrationForm()
    content = {'register_form': register_form, 'title': title}
    return render(request, 'authapp/register.html', content)


def login(request):
    title = 'Login'
    login_form = TravelUserLoginForm(data=request.POST or None)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main:main'))
    content = {
        'title': title,
        'login_form': login_form,
        'next': next
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main'))


@transaction.atomic()
def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = TravelUserEditForm(request.POST,
                                       request.FILES, instance=request.user)
        profile_form = TravelUserProfileEditForm(
            request.POST, instance=request.user.traveluserprofile)

        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = TravelUserEditForm(instance=request.user)
        profile_form = TravelUserProfileEditForm(instance=
                                                 request.user.traveluserprofile)

    content = {'title': title,
               'edit_form': edit_form,
               'profile_form': profile_form}

    return render(request, 'authapp/edit.html', content)
