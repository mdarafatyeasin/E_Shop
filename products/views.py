from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddProductForm,CommentForm
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
    pk_url_kwarg = 'id'
    template_name = 'product_detail.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        product = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        comments = product.comment.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context