# Generated by Django 2.1.2 on 2018-10-04 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='provedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=200)),
                ('rfc', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=100)),
                ('domicilio', models.TextField(max_length=200)),
                ('mision', models.TextField(max_length=4000)),
                ('vision', models.TextField(max_length=4000)),
                ('fecha_registro', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
