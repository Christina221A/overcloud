# Generated by Django 3.1.3 on 2020-12-12 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='webapp/img/icon-dark.png', upload_to='webapp/media'),
        ),
    ]
