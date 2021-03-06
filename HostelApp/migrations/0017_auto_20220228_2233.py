# Generated by Django 3.2.9 on 2022-02-28 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HostelApp', '0016_alter_room_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='in_charge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HostelApp.matron'),
        ),
        migrations.AlterField(
            model_name='room',
            name='occupant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HostelApp.student'),
        ),
    ]
