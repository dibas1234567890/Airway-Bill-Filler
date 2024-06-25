from django import forms
from typing import Any, Mapping, __all__

from awbfillerapp.models import airwayBill

class awb_form(forms.ModelForm):
    
    class Meta:
        model = airwayBill
        fields = ("__all__")
    
    