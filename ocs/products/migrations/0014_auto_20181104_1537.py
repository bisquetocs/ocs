# Generated by Django 2.1.2 on 2018-11-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20181104_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]