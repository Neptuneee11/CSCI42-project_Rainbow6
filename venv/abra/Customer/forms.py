from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=100, required=True)
    last_name = forms.CharField(label="Last Name", max_length=100, required=True)
    email = forms.EmailField(required=True)
    id_number = forms.CharField(label="ID Number", max_length=20, required=True)
    school_year = forms.CharField(label="School Year", max_length=20, required=True)
    course = forms.CharField(label="Course", max_length=50, required=True)
    phone_number = forms.CharField(label="Phone Number", max_length=15, required=True)
    

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "id_number", "school_year", "course",  "password1", "password2", "phone_number"]

