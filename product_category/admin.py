from django.contrib import admin
from .models import productCategory
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('categoryName',)}

admin.site.register(productCategory, categoryAdmin)