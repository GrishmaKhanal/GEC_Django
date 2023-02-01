from django import forms
from .models import *


# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     email = forms.EmailField(required=False, label='Your e-mail address')
#     message = forms.CharField(widget=forms.Textarea)

class InputText(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your text...', 'class':'form-control', 'rows':'20', 'cols':'70'}))
    class Meta:
        model = WritingCoach
        fields = '__all__'