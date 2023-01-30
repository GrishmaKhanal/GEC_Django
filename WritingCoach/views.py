from django.shortcuts import render
from django.http import HttpResponse

from .forms import *    # * -> InputText, ContactForm

def home(request):
    if request.method == 'POST':
        form = InputText(request.POST)
        form.save()
        description = form.cleaned_data['description']
        changed_description = description.upper()
        return render(request, 'index.html', {'description': description, 'changed_description': changed_description})
    else:
        form = InputText()
    return render(request, 'home.html', {'form': form})

# def about(request):
#     return render(request, 'about.html')


# def get_input(request):
#     if request.method == 'POST':
#         form = InputText(request.POST)
#         form.save()
#         return True
#     else:
#         form = InputText()
#     return True