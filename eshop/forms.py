from django.forms import ModelForm
from .models.products import Product
from .models.orders import Order
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['ismi', 'price', 'rasmi', 'category']
    
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'narxi','count']
