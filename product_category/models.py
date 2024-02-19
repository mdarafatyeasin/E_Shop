from django.db import models

# Create your models here.
class productCategory (models.Model):
    categoryName = models.CharField(max_length = 100, null=True, blank=True)
    slug = models.SlugField(max_length = 100, null=True, blank=True, unique = True)

    def __str__ (self):
        return self.categoryName