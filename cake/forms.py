from django import forms
from . models import SignUp



class UserRegistrationForm(forms.ModelForm):
    
    fullname=forms.CharField(widget=forms.TextInput(attrs={'class':'border h-10 w-80 mb-5'}))
    emailaddress=forms.CharField(widget=forms.TextInput(attrs={'class': 'border h-10 w-80 mb-5'}))
    phonenumber=forms.CharField(widget=forms.TextInput(attrs={'class':'border h-10 w-80 mb-5'}))
    location=forms.CharField(widget=forms.TextInput(attrs={'class':'border h-10 w-80 mb-5'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'border h-10 w-80 mb-5'}))
   

    class Meta:
        model= SignUp
        fields=('fullname','emailaddress','phonenumber','location','password')
    

class LoginForm(forms.Form):
    emailaddress = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
