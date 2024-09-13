from django.db import models


class Product(models.Model):
    name = models.CharField(null=False, max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=True,decimal_places=2,max_digits=10)