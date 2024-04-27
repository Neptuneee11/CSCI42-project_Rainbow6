from django import forms
from django.contrib.auth import login, authenticate
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=100, required=True)
    last_name = forms.CharField(label="Last Name", max_length=100, required=True)
    email = forms.EmailField(label="Email (e.g. '-@mail.com')", max_length=100, required=True)
    id_number = forms.IntegerField(label="ID Number (e.g. '123456')", required=True, validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    school_year = forms.CharField(label="School Year (e.g. 'Third Year')", max_length=20, required=True)
    course = forms.CharField(label="Course (e.g. 'Computer Science')", max_length=50, required=True)
    phone_number = forms.IntegerField(label="Phone Number (e.g. '09xxxxxxxxx')", required=True, validators=[MinValueValidator(10000000000), MaxValueValidator(99999999999)])
    

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "phone_number", "id_number", "school_year", "course",  "password1", "password2"]

