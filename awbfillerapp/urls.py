
from awbfillerapp.views.view_awbs import awbView
from awbfillerapp.views.homepageformview import index
from awbfillerapp.views.pdfExporter import pdfExport
from django.urls import path


urlpatterns = [
    path('', index.form), 
    path('pdfexport/<int:id>/',pdfExport.exporter, name='export' ), 
    path('viewawbs/',awbView.viewer, name='viewer' ), 

]
