# Generated by Django 3.2.9 on 2022-03-06 20:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HostelApp', '0025_auto_20220306_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='post_image'),
        ),
    ]
