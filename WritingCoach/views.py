from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
    if request.method == 'POST':
        description = request.POST.get('input-description')
        changed_description = description.upper()
        return render(request, 'home.html', {'description': description, 'changed_description': changed_description})
    else:  
        return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')