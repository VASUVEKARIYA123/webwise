# Generated by Django 5.0.3 on 2024-03-26 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='discpunt_deal',
            new_name='discount_deal',
        ),
    ]
