# Generated by Django 4.2.1 on 2023-07-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0007_orders_key_alter_basket_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='key',
            field=models.CharField(default='your_default_value', max_length=128),
        ),
    ]
