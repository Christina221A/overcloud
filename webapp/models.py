from django.db import models

# Create your models here.
class Cart(models.Model):
    p_id = models.IntegerField()
    p_amount = models.IntegerField(default=0)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sort = models.IntegerField(default=0) #drink:0, food:1
