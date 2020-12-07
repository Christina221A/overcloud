from django.db import models


# Create your models here.

class Users(models.Model):
    """docstring for Users"""
    # 用户名必填，最长不超过128个字符且唯一
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    # create_time 用户被创建的时间
    c_time = models.DateTimeField(auto_now_add=True)

    # 使用__str__人性化显示对象信息
    def __str__(self):
        return self.name

    # 元数据里，定义用户按创建时间的反序排列
    # aka 最近创建的最先显示
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
