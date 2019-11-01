from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import MyUser
from django.contrib.auth import get_user_model


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    
    def clean_email(self):
        User = get_user_model()
        
        user_provided_email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=user_provided_email):
            raise forms.ValidationError("This email address is already in use")
        
        return user_provided_email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise forms.ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
            
        return password2
        
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password1', 'password2']