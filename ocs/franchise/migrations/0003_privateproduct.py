# Generated by Django 2.1.2 on 2018-10-24 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('franchise', '0002_auto_20181008_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('id_franchise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='franchise.Franchise')),
            ],
        ),
    ]
