from django import forms
from .models import userTransaction

class DepositForm(forms.ModelForm):
    class Meta:
        model = userTransaction
        fields = ['amount']