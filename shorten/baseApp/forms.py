from django import forms
from .models import URLDB
from django.db import models
class ShortUrlForm(forms.ModelForm):
    class Meta:
        model = URLDB
        exclude = ('shortenedUrl',)
        error_messages = {
            'originalUrl': {'unique':('This Url is already shortened...Please Check the home page.')}
        }
    def __init__(self, *args, **kwargs):
        super(ShortUrlForm, self).__init__(*args, **kwargs)
        self.fields['originalUrl'].widget.attrs.update({
            
            'class': 'form-control',
            'placeholder': 'Paste the URL here!!!'})
        self.fields['originalUrl'].label = ''
