# Generated by Django 2.2 on 2020-07-16 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20200715_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busunit',
            name='location',
            field=models.ForeignKey(default='No disponible', on_delete=django.db.models.deletion.SET_DEFAULT, to='API.BusStop'),
        ),
    ]
