from django.db import models


class Cart(models.Model):  # 购物车主表
    user_id = models.IntegerField()  # 用户id
    status = models.BooleanField(default=False)


class CartDetail(models.Model):  # 购物车明细
    cart_id = models.IntegerField()  # 对应 Cart 的id
    product_id = models.IntegerField()
    quantity = models.IntegerField(default=0)


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sort = models.IntegerField(default=0)  # drink:0, food:1
    image = models.ImageField(upload_to='webapp/media', default="img/icon-dark.png")

    def __str__(self):
        return self.name
