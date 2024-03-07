# Generated by Django 5.0.2 on 2024-02-21 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('add_id', models.IntegerField(primary_key=True, serialize=False)),
                ('street_address', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.IntegerField(max_length=6)),
                ('currunt_location', models.DateField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bank_details',
            fields=[
                ('bank_acc_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ifsc_code', models.CharField(max_length=100)),
                ('acc_holder_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_fname', models.CharField(max_length=100)),
                ('c_mname', models.CharField(max_length=100)),
                ('c_lname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pay_date', models.DateTimeField()),
                ('pay_mode', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100)),
                ('p_disc', models.CharField(max_length=100)),
                ('quantity_per_unit', models.IntegerField(max_length=10)),
                ('price', models.IntegerField(max_length=10)),
                ('weight', models.IntegerField(max_length=10)),
                ('unit_in_stock', models.IntegerField(max_length=10)),
                ('unit_in_order', models.IntegerField(max_length=10)),
                ('discount', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('shipper_id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=10)),
                ('company_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('u_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('num_of_products', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('o_id', models.IntegerField(primary_key=True, serialize=False)),
                ('num_of_products', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('o_status', models.CharField(max_length=100)),
                ('o_date', models.DateTimeField()),
                ('o_shipped_date', models.DateTimeField()),
                ('add_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.address')),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.customer')),
                ('pay_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.payment')),
                ('shipper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.shipper')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_info',
            fields=[
                ('per_info_id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone', models.IntegerField(verbose_name=10)),
                ('bank_acc_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.bank_details')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='per_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.personal_info'),
        ),
        migrations.AddField(
            model_name='address',
            name='per_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.personal_info'),
        ),
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('od_id', models.IntegerField(primary_key=True, serialize=False)),
                ('unitprice', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('discount', models.IntegerField(max_length=2)),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.order')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('i_id', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='pics')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_products',
            fields=[
                ('cp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.cart')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.IntegerField(primary_key=True, serialize=False)),
                ('report_desc', models.CharField(max_length=100)),
                ('report_type', models.CharField(max_length=100)),
                ('report_date', models.DateTimeField()),
                ('report_satatus', models.CharField(max_length=20)),
                ('resolve_date', models.DateTimeField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('r_id', models.IntegerField(primary_key=True, serialize=False)),
                ('r_des', models.CharField(max_length=100)),
                ('r_grade', models.IntegerField(max_length=1)),
                ('r_date', models.DateTimeField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.customer')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('s_id', models.IntegerField(primary_key=True, serialize=False)),
                ('contact_email', models.CharField(max_length=100)),
                ('contact_fname', models.CharField(max_length=100)),
                ('contact_mname', models.CharField(max_length=100)),
                ('contact_lname', models.CharField(max_length=100)),
                ('contact_title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('verified', models.BooleanField(default=True)),
                ('per_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.personal_info')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.salesman'),
        ),
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('cupon_id', models.IntegerField(primary_key=True, serialize=False)),
                ('discount', models.IntegerField(max_length=2)),
                ('cupon_use_number', models.IntegerField()),
                ('cupon_max_use_number', models.IntegerField()),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.salesman')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('w_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist_products',
            fields=[
                ('wp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.product')),
                ('w_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.wishlist')),
            ],
        ),
    ]