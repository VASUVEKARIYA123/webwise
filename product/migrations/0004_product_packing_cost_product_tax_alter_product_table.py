# Generated by Django 5.0.3 on 2024-03-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='packing_cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterModelTable(
            name='product',
            table='product_Product',
        ),
    ]
