# Generated by Django 5.0.3 on 2024-04-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='Product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='Product_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
