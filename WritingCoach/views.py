from django.shortcuts import render

from .models import *
import re

def home(request):
    if request.method == 'POST':
        description = request.POST.get('input-description')
        unclean_description = predict_error(predict_error(description))
        cleaned_description = re.sub(r'(<pad>|<unk>|<s>|</s>)','', unclean_description)
        changed_description = cleaned_description[1:]
        return render(request, 'home.html', {'description': description, 'changed_description': changed_description})
    else:  
        return render(request, 'home.html')
