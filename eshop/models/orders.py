from django.db import models
from .products import Product
class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    narxi = models.PositiveBigIntegerField()
    count = models.PositiveBigIntegerField()

    