from django.shortcuts import render,redirect
from .forms import addProductCategory
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_category(request):
    if request.method == "POST":
        add_category_form = addProductCategory(request.POST)
        if add_category_form.is_valid():
            messages.success(request, "category added successfully")
            add_category_form.save()
            return redirect("add_category")
    else:
        add_category_form = addProductCategory()
    return render (request, 'add_category.html', {"form":add_category_form})