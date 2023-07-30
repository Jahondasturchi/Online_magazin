from django.db import models
from .categories import Categor


class Product(models.Model):
    ismi = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    rasmi = models.ImageField(null=True, blank=True, upload_to='images')
    category = models.ForeignKey(Categor, on_delete=models.CASCADE)