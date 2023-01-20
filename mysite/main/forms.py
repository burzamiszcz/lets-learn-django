from django import forms
from .models import Ad


class CreateNewAd(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['name','text']