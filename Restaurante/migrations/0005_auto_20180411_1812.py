# Generated by Django 2.0.4 on 2018-04-11 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0004_auto_20180411_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favourites',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='preferences',
        ),
        migrations.AddField(
            model_name='profile',
            name='preferences',
            field=models.CharField(choices=[('a', 'Hola'), ('b', 'Hello'), ('c', 'Bonjour'), ('d', 'Boas')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
