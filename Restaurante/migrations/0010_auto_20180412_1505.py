# Generated by Django 2.0.3 on 2018-04-12 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0009_auto_20180411_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='specific',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
