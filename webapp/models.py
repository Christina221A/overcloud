from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import uuid
import os


def product_media_path(product, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    # return the whole path to the file
    return os.path.join(product.name, "media", filename)


class Cart(models.Model):  # 购物车主表
    user_id = models.IntegerField()  # 用户id
    status = models.BooleanField(default=False)


class CartDetail(models.Model):  # 购物车明细
    cart_id = models.CharField(max_length=128)  # 对应 Cart 的id
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sort = models.IntegerField(default=0)  # drink:0, food:1
    image = ProcessedImageField(upload_to=product_media_path,
                                processors=[ResizeToFill(100, 100)],
                                format='PNG',
                                options={'quality': 100})

    def __str__(self):
        return self.name
