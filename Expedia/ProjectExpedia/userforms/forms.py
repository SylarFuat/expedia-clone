from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class UserFormCreate(forms.Form):
    username = forms.CharField(max_length=100, label='Your Name', required=True)
    email = forms.EmailField(max_length=100, label='Your Email', required=True)
    password1 = forms.CharField(label='Your Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Your Password', widget=forms.PasswordInput, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match!')
    
        return cleaned_data
    
    def save(self):
        user = User.objects.create_user(
            username = self.cleaned_data['username'],
            email = self.cleaned_data['email'],
            password= self.cleaned_data['password1'],
        )
        return user
    
class UserFormLogin(forms.Form):
    username = forms.CharField(max_length=120, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)