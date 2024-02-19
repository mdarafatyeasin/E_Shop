from django import forms
from .models import Product,Comment

class AddProductForm (forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __str__(self):
        return self.name
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']