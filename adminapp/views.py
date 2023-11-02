from django.contrib.auth.decorators import user_passes_test
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import TravelUserAdminEditForm, AccommodationEditForm
from authapp.forms import TravelUserRegistrationForm
from authapp.models import TravelUser
from mainapp.models import ListOfCountries, Accommodation


class TravelUserListView(ListView):
    model = TravelUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'создание пользователя'

    if request.method == 'POST':
        user_form = TravelUserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = TravelUserRegistrationForm()

    content = {
        'title': title,
        'update_form': user_form
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'редактирование пользователя'

    edit_user = get_object_or_404(TravelUser, pk=pk)

    if request.method == 'POST':
        edit_form = TravelUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = TravelUserAdminEditForm(instance=edit_user)
    content = {
        'title': title,
        'update_form': edit_form
    }
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request: WSGIRequest, pk: int):
    title = 'удаление пользователя'
    user = get_object_or_404(TravelUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {
        'title': title,
        'user_to_delete': user
    }
    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def countries(request: WSGIRequest):
    title = 'Страны'

    countries_list = ListOfCountries.objects.all()
    content = {
        'title': title,
        'objects': countries_list
    }
    return render(request, 'adminapp/countries.html', content)


class CountryCreateView(CreateView):
    model = ListOfCountries
    template_name = 'adminapp/country_update.html'
    success_url = reverse_lazy('admin:countries')
    fields = '__all__'


class CountryUpdateView(UpdateView):
    model = ListOfCountries
    template_name = 'adminapp/country_update.html'
    success_url = reverse_lazy('admin:countries')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'редактирование страны'
        return context


class CountryDeleteView(DeleteView):
    model = ListOfCountries
    template_name = 'adminapp/country_delete.html'
    success_url = reverse_lazy('admin:countries')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.success_url())


@user_passes_test(lambda u: u.is_superuser)
def accommodations(request, pk):
    title = 'размещение'

    country = get_object_or_404(ListOfCountries, pk=pk)
    accommodation_list = Accommodation.objects.filter(country__id=pk).order_by('name')
    content = {
        'title': title,
        'country': country,
        'objects': accommodation_list
    }
    return render(request, 'adminapp/accommodations.html', content)


@user_passes_test(lambda u: u.is_superuser)
def accommodation_create(request, pk):
    title = 'создание размещения'
    country = get_object_or_404(ListOfCountries, pk=pk)

    if request.method == 'POST':
        accommodation_form = AccommodationEditForm(request.POST, request.FILES)
        if accommodation_form.is_valid():
            accommodation_form.save()
            return HttpResponseRedirect(reverse('admin:accommodations', args=[pk]))
    else:
        accommodation_form = AccommodationEditForm(initial={'country': country})
    content = {
        'title': title,
        'country': country,
        'update_form': accommodation_form
    }
    return render(request, 'adminapp/accommodation_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def accommodation_update(request, pk):
    title = 'изменение размещения'
    edit_accommodation = get_object_or_404(Accommodation, pk=pk)

    if request.method == 'POST':
        accommodation_edit_form = AccommodationEditForm(request.POST, request.FILES, instance=edit_accommodation)
        if accommodation_edit_form.is_valid():
            accommodation_edit_form.save()
            return HttpResponseRedirect(reverse('admin:accommodation_update', args=[edit_accommodation.pk]))
    else:
        accommodation_edit_form = AccommodationEditForm(instance=edit_accommodation)
    content = {
        'title': title,
        'update_form': accommodation_edit_form,
        'country': edit_accommodation.country
    }
    return render(request, 'adminapp/accommodation_update.html', content)


class AccommodationDetailView(DetailView):
    model = Accommodation
    template_name = 'adminapp/accommodation_read.html'


@user_passes_test(lambda u: u.is_superuser)
def accommodation_delete(request, pk):
    title = 'удаление размещения'
    accommodation = get_object_or_404(Accommodation, pk=pk)
    if request.method == 'POST':
        accommodation.is_active = False
        accommodation.save()
        return HttpResponseRedirect(reverse('admin:accommodations', args=[accommodation.country.pk]))

    content = {
        'title': title,
        'accommodation_to_delete': accommodation,
    }
    return render(request, 'adminapp/accommodation_delete.html', content)


