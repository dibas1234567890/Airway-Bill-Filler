
from awbfillerapp.views.homepageformview import index
from awbfillerapp.views.pdfExporter import pdfExport
from django.urls import path


urlpatterns = [
    path('', index.form), 
    path('pdfexport/',pdfExport.exporter, name='export' ), 

]
