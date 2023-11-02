from django import forms

from authapp.forms import TravelUserEditForm
from authapp.models import TravelUser
from mainapp.models import ListOfCountries, Accommodation


class TravelUserAdminEditForm(TravelUserEditForm):
    class Meta:
        model = TravelUser
        fields = '__all__'


class ListOfCountriesEditForm(forms.ModelForm):
    class Meta:
        model = ListOfCountries
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class AccommodationEditForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
