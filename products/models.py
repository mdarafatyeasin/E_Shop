from django.db import models
from product_category.models import productCategory
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    category = models.ForeignKey(productCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.CharField(max_length = 10)
    quantity = models.CharField(max_length = 10)
    picture = models.ImageField(upload_to="products/product_img", null=True, blank=True)

    def __str__(self):
        return self.product_name
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'comment')
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name