from django.urls import path
from .views import add_product,ProductDetails

urlpatterns = [
    path("add_product", add_product, name="add_product"),
    path("product_details/<int:id>", ProductDetails.as_view(), name="product_details"),
]