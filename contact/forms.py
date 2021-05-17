from django import forms

class Registration(forms.Form):
    name = forms.CharField(max_length=100 , label="Name :")
    email = forms.EmailField(max_length=100 , label="Email :")
    password = forms.CharField(max_length=100 , label="Password :")
    note = forms.CharField(widget=forms.Textarea ,label="Note")

  
