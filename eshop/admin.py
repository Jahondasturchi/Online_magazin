from django.contrib import admin
from .models.categories import Categor
from .models.products import Product
from .models.orders import Order
# Register your models here.
admin.site.register(Categor)
admin.site.register(Product)
admin.site.register(Order)