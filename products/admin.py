from django.contrib import admin
from .models import Category, Tag, Product

#adds each to admin panel
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
