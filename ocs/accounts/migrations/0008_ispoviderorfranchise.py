# Generated by Django 2.1.2 on 2018-10-12 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('accounts', '0007_auto_20181009_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='IsPoviderOrFranchise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_provider', models.BooleanField(default=False)),
                ('is_franchise', models.BooleanField(default=False)),
                ('id_admin', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
    ]