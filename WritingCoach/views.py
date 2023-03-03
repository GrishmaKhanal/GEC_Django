from django.shortcuts import render

from .models import *
import re

def home(request):
    if request.method == 'POST':
        description = request.POST.get('input-description')
        unclean_description = predict_error(predict_error(description))
        changed_description = re.sub(r'(<pad>|<unk>|<s>|</s>)','', unclean_description)
        
        return render(request, 'home.html', {'description': description, 'changed_description': changed_description})
    else:  
        return render(request, 'home.html')
