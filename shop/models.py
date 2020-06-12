from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Product(models.Model):
    article = models.IntegerField()
    productName = models.CharField(max_length=200, default="")
    text = models.TextField(default="")

    def __str__(self):
        return self.productName