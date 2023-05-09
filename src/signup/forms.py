from django import forms

class Signup_Form(forms.Form):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.widgets.PasswordInput())
    password_check = forms.CharField(label='Password Check', widget=forms.widgets.PasswordInput())
