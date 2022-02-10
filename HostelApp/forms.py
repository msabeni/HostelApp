from django import forms
from django.db import transaction
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 

class matron_signup(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    profile_pic = CloudinaryField()

    class Meta (UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
            user = super().save(commit=False)
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.is_matron = True
            user.save()
            matron = Matron.objects.create(user=user)
            matron.email_address = self.cleaned_data.get('email_address')
            matron.phone_number = self.cleaned_data.get('phone_number')
            matron.profile_pic = self.cleaned_data.get('profile_pic')
            return matron
        

class student_signup(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    registration_no = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    profile_pic = CloudinaryField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')        
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.registration_no = self.cleaned_data.get('reg_no')
        student.email = self.cleaned_data.get('email')
        student.phone_number = self.cleaned_data.get('phone_number')
        student.profile_pic = self.cleaned_data.get('profile_pic')

        return student