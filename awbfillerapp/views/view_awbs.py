from django.shortcuts import render
from django.views import View
from awbfillerapp.models import airwayBill
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class awbView(View):
    def viewer(request):
        objects_list = airwayBill.objects.all()
        p = Paginator(objects_list, 10)
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)
        context = {'page_obj': page_obj}
        
        return render(request, 'viewawb.html', context)