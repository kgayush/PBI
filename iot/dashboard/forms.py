from django import forms
from matplotlib import style
from .models import Data
 
class MyForm(forms.ModelForm):
  class Meta:
    model = Data
    fields = ["floor", "room", "product", "status",]
    labels = {"floor": "Floor", "room": "Room No", "product": "Appliance", "status": "Status",}
    style = {}