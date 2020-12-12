from django.contrib import admin

# Register your models here.
from .models import Cart, Product, CartDetail

admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(CartDetail)
