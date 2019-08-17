from django import forms
from .models import short_urls

class UrlForm (forms.ModelForm):
    class Meta:
        model = short_urls
        fields = ['long_url','short_url']

class search(forms.Form):
    URL = forms.URLField()

