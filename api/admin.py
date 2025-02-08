from django.contrib import admin
from .models import Category, Product, ProductImage, Size, Color


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Size)
admin.site.register(Color)