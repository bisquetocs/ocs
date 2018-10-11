# Generated by Django 2.1.2 on 2018-10-09 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181009_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocsuser',
            name='id_franchise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='franchise.Franchise'),
        ),
        migrations.AlterField(
            model_name='ocsuser',
            name='id_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provider.Provider'),
        ),
    ]
