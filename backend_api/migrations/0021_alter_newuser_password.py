# Generated by Django 4.2.1 on 2023-11-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0020_remove_material_idproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]