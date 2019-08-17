from django import forms
from .models import short_urls

class search(forms.ModelForm):
    class Meta:
        model = short_urls
        fiels = ['long_url']