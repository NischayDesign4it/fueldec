from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, vehicle



class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class TankForm(forms.ModelForm):
    class Meta:
        model = vehicle
        fields = ['vehicleNumber']

