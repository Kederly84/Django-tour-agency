from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from authapp.models import TravelUser, TravelUserProfile


class CleanAgeMixin(forms.ModelForm):
    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('You are too young!!!')
        return data


class TravelUserRegistrationForm(UserCreationForm):
    class Meta:
        model = TravelUser
        fields = (
            'username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
            filed.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('You are too young!!!')
        return data


class TravelUserEditForm(UserChangeForm):
    class Meta:
        model = TravelUser
        fields = (
            'username', 'first_name', 'email', 'age', 'avatar', 'password'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('You are too young!!!')
        return data


class TravelUserLoginForm(AuthenticationForm):
    class Meta:
        model = TravelUser
        fields = (
            'username', 'password'
        )

    def __init__(self, *args, **kwargs):
        super(TravelUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class TravelUserProfileEditForm(forms.ModelForm):
    class Meta:
        model = TravelUserProfile
        fields = ('tagline', 'about_me', 'gender')

    def __init__(self, *args, **kwargs):
        super(TravelUserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
