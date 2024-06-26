from django import forms
from typing import Any, Mapping, __all__

from awbfillerapp.models import airwayBill

class awb_form(forms.ModelForm):
    flight_date = forms.DateField(widget=forms.SelectDateWidget)
    flight_date_carrier = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = airwayBill
        fields = ("__all__")
    
    