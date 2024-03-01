from django import forms
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'place', 'date', 'time']

class Registration(forms.Form):
    username = forms.CharField(label='Ім`я користувача', max_length=150)
    email = forms.EmailField(label='Електронна пошта', max_length=254, help_text='Введіть адресу електронної пошти.')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Користувач з таким ім`ям вже існує.")
        return username

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        return user