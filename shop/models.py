from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class shop_model (models.Model):
        author_name = models.ForeignKey(User, on_delete = models.CASCADE)
        product_id = models.CharField(max_length=50, default='default_value')

        def __str__(self):
                return f"Author: {self.author_name} | Product: {self.product_id}"