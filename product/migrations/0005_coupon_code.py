# Generated by Django 5.0.3 on 2024-03-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_packing_cost_product_tax_alter_product_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon_Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
                ('max_use', models.IntegerField()),
                ('total_used', models.IntegerField()),
            ],
        ),
    ]
