# Generated by Django 3.1.3 on 2020-12-12 05:54

from django.db import migrations
import imagekit.models.fields
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20201212_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=webapp.models.product_media_path),
        ),
    ]
