from django import forms
from django.forms import DateInput


class NailMasterForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    price_per_hour = forms.DecimalField(label='Price per hour', max_digits=10, decimal_places=2)
    category = forms.CharField(label='category')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class ReviewForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)


class AppointmentsForm(forms.Form):
    date = forms.DateField(label='Date')
