from django import forms  
from .models import Staff

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Staff
        fields = ('username', 'password', 'password_confirmation')