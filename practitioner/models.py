from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


TITLE_CHOICES = [
                  ('DOCTOR', 'Doctor'),
                  ('NURSE', 'Nurse')
                ]  

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    designation = models.CharField(max_length=6, choices=TITLE_CHOICES, default='DOCTOR')

    def __str__(self):
        return f'{self.user.username} Profile'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname',  'designation']

class UserRegistrationForm(UserCreationForm):  
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


