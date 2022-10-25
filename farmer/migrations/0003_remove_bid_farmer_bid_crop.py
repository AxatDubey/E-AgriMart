# Generated by Django 4.1.2 on 2022-10-13 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0002_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='farmer',
        ),
        migrations.AddField(
            model_name='bid',
            name='crop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='farmer.product'),
        ),
    ]
