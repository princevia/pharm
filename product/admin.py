from msilib.schema import Media
from unicodedata import category
from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
