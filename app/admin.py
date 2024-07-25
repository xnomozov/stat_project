from django.contrib import admin

from app.models import Product, Customer, Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)