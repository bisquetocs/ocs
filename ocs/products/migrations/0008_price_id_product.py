# Generated by Django 2.1.2 on 2018-11-04 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181102_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='id_product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
    ]