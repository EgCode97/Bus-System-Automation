# Generated by Django 2.2 on 2020-07-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0010_auto_20200716_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route',
            field=models.CharField(max_length=150, verbose_name='Route Name'),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_description',
            field=models.CharField(default='No disponible', max_length=150, verbose_name='Route description'),
        ),
    ]
