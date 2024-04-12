# Generated by Django 4.2.1 on 2023-07-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0004_alter_orders_address_alter_orders_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=225),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(default='', max_length=225),
        ),
        migrations.AlterField(
            model_name='orders',
            name='comments',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(default='', max_length=225),
        ),
        migrations.AlterField(
            model_name='orders',
            name='firstName',
            field=models.CharField(default='', max_length=225),
        ),
        migrations.AlterField(
            model_name='orders',
            name='lastName',
            field=models.CharField(default='', max_length=225),
        ),
        migrations.AlterField(
            model_name='orders',
            name='patronymic',
            field=models.CharField(default='', max_length=225),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=225),
        ),
        migrations.AlterField(
            model_name='orders',
            name='product_id',
            field=models.CharField(default='', max_length=225),
        ),
        migrations.AlterField(
            model_name='orders',
            name='quantity',
            field=models.CharField(default='', max_length=225),
        ),
    ]
