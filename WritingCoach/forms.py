from django import forms

class InputText(forms.Form):
    text = forms.CharField(label='Enter text', widget=forms.Textarea(attrs={'rows':10, 'cols':30}))

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)