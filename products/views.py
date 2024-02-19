from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddProductForm
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from .models import Product

# Create your views here.
@login_required
def add_product(request):
    if request.method == "POST":
        add_product_form = AddProductForm(request.POST, request.FILES)
        if add_product_form.is_valid():
            messages.success(request, "Car Added")
            add_product_form.save()
            return redirect("add_product")
    else:
        add_product_form = AddProductForm()
    return render(request, "add_product.html", {"form": add_product_form})

# detail
@method_decorator(login_required, name='dispatch')
class ProductDetails(DetailView):
    model = Product
    pk_url_kwarg = "id"
    template_name = "product_detail.html"
    def get(self, request, *args, **kwargs):
        # Access and print the current user's ID
        user_id = request.user.id
        print(request.user.id)
        return super().get(request, *args, **kwargs)