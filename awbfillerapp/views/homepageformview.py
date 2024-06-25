from django.shortcuts import render
from django.views import View
from fillpdf import fillpdfs

from awbfillerapp.forms import awb_form

class index(View):
    def form(request):
        form = awb_form(request.POST)
        if form.is_valid():
            form.save()
            form = awb_form()
            return render(request, 'index.html', {'form':form})
        
        return render(request, 'index.html', {'form':form})
    
