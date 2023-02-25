from django.shortcuts import render

from .models import *

def home(request):
    if request.method == 'POST':
        description = request.POST.get('input-description')
        changed_description = predict_error(description)
        return render(request, 'home.html', {'description': description, 'changed_description': changed_description})
    else:  
        return render(request, 'home.html')
