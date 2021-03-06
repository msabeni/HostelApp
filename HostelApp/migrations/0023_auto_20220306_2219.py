# Generated by Django 3.2.9 on 2022-03-06 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HostelApp', '0022_announcement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='room',
        ),
        migrations.AddField(
            model_name='student',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_owner', to='HostelApp.room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='occupant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned', to='HostelApp.student'),
        ),
    ]
