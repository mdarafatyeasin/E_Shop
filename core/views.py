from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product
from product_category.models import productCategory
# Create your views here.

def HomePage (request,category_slug = None) :
    all_products = Product.objects.all()
    all_categories = productCategory.objects.all()
    if category_slug is not None:
        product_category = productCategory.objects.get(slug = category_slug)
        all_products = Product.objects.filter(category = product_category)

    return render (request, 'index.html', {"all_products":all_products, "all_categories":all_categories})