# Generated by Django 2.2 on 2020-07-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0012_auto_20200716_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='description',
            field=models.CharField(default='Ubicacion de la zona', help_text='Alcance y ubicacion de la zona', max_length=150),
            preserve_default=False,
        ),
    ]