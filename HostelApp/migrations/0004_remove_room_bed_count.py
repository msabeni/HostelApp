# Generated by Django 3.2.9 on 2022-02-19 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HostelApp', '0003_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='bed_count',
        ),
    ]