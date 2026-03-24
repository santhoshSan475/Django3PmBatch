from django import forms
from .models import CustomerModel

class customerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = "__all__"


