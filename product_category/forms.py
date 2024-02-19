from django import forms
from .models import productCategory

class addProductCategory(forms.ModelForm):
    class Meta:
        model = productCategory
        fields = ['categoryName']