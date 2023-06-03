from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class AddOwn(forms.Form):
    name = forms.CharField(label="Name")
    package = forms.IntegerField(label="Number of package")
    drug = forms.CharField(label="Name of drug")
    phone = forms.IntegerField(label="Phone number")
    address = forms.CharField(label="Address")
