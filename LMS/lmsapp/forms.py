from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Course, Blog, Lesson, Video, Certificate
from django.forms import inlineformset_factory

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder":"Username/Email",
                "class":"form-control",
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder":"Password",
            }
        )
    )

class SignUpForm(UserCreationForm):
    
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder":"Username",
                "class": "form-control",                
            }
        )
    )
    
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class":"form-control",
                "placeholder":"Password"
            }
        )
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class":"form-control",
                "placeholder":"Confirm Password"
            }
        )
    )
    email = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class":"form-control",
                "placeholder":"example@gmail.com"
            }
        )
    )
   
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_student', 'is_instructor', 'is_manager')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'email', 'user_bio']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['username', 'course_name', 'instructor_name']