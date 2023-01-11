from django import forms

class CreateNewUser(forms.Form):
    username = forms.CharField(label = "username", max_length=50)