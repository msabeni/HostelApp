# Generated by Django 3.2.9 on 2022-02-21 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HostelApp', '0007_alter_room_occupant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='occupant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostelApp.student'),
        ),
    ]
