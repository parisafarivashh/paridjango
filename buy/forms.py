from django import forms
class RegistrationForm(forms.Form):
  username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    'class':'form_control',
    'placeholder':'username'
  }))
  password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
    'class':'form_control',
    'placeholder':'password'
  }))
  email = forms.CharField(max_length=100,widget=forms.EmailInput(attrs={
    'class':'form_control',
    'placeholder':'email'

  }))
  phone = forms.CharField(max_length=30,widget=forms.NumberInput(attrs={
    'class':'form_control',
    'placeholder':'phone'
  }))
