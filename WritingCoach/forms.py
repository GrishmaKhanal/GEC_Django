from django import forms
from .models import *


# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     email = forms.EmailField(required=False, label='Your e-mail address')
#     message = forms.CharField(widget=forms.Textarea)

class InputText(forms.ModelForm):
    class Meta:
        model = WritingCoach
        fields = '__all__'