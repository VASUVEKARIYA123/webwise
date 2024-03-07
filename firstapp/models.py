from django.db import models

# Create your models here.

class User(models.Model):
    u_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=100)
    u_email = models.CharField(max_length=100)

class Bank_details(models.Model):
    bank_acc_no = models.CharField(max_length=100, primary_key=True)
    ifsc_code = models.CharField(max_length=100)
    acc_holder_name= models.CharField(max_length=100)

class Personal_info(models.Model):
    per_info_id = models.IntegerField(primary_key=True)
    phone = models.IntegerField(10)
    bank_acc_no = models.ForeignKey(Bank_details, on_delete=models.CASCADE)

class Address(models.Model):
    add_id = models.IntegerField(primary_key=True)
    per_info_id = models.ForeignKey(Personal_info,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.IntegerField(max_length=6)
    currunt_location = models.DateField(max_length=200)

class Customer(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_fname = models.CharField(max_length=100)
    c_mname = models.CharField(max_length=100)
    c_lname = models.CharField(max_length=100)
    per_info_id = models.ForeignKey(Personal_info, on_delete=models.CASCADE)

class Salesman(models.Model):
    s_id = models.IntegerField(primary_key=True)
    contact_email= models.CharField(max_length=100)
    contact_fname=models.CharField(max_length=100)
    contact_mname=models.CharField(max_length=100)
    contact_lname=models.CharField(max_length=100)
    contact_title=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    verified = models.BooleanField(default=True)
    per_info_id = models.ForeignKey(Personal_info, on_delete=models.CASCADE)

class Product(models.Model):
    p_id = models.IntegerField(primary_key=True)
    s_id= models.ForeignKey(Salesman, on_delete=models.CASCADE)
    p_name =models.CharField(max_length=100)
    p_disc =models.CharField(max_length=100)
    quantity_per_unit =models.IntegerField(max_length=10)
    price =models.IntegerField(max_length=10)
    weight =models.IntegerField(max_length=10)
    unit_in_stock =models.IntegerField(max_length=10)
    unit_in_order =models.IntegerField(max_length=10)
    discount =models.IntegerField(max_length=2)
    
class images(models.Model):
    i_id = models.IntegerField(primary_key=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='pics')

class Wishlist(models.Model):
    w_id = models.IntegerField(primary_key=True)
    c_id = models.ForeignKey(Customer,on_delete=models.CASCADE)

class Wishlist_products(models.Model):
    wp_id=models.IntegerField(primary_key=True)
    w_id = models.ForeignKey(Wishlist,on_delete=models.CASCADE)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Review(models.Model):
    r_id = models.IntegerField(primary_key=True)
    c_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    r_des = models.CharField(max_length=100)
    r_grade = models.IntegerField(max_length=1)
    r_date = models.DateTimeField()
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    c_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    num_of_products = models.IntegerField()
    total_price = models.IntegerField()

class Cart_products(models.Model):
    cp_id = models.IntegerField(primary_key=True)
    cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Shipper(models.Model):
    shipper_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10)
    company_email = models.CharField(max_length=100)

class Payment(models.Model):
    pay_id = models.IntegerField(primary_key=True)
    pay_date = models.DateTimeField()
    pay_mode = models.CharField(max_length=20)
    price = models.IntegerField()

class Order(models.Model):
    o_id = models.IntegerField(primary_key=True)
    c_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    pay_id = models.ForeignKey(Payment,on_delete=models.CASCADE)
    num_of_products = models.IntegerField()
    total_price = models.IntegerField()
    o_status = models.CharField(max_length=100)
    o_date = models.DateTimeField()
    o_shipped_date = models.DateTimeField()
    add_id = models.ForeignKey(Address,on_delete=models.CASCADE)
    shipper_id = models.ForeignKey(Shipper,on_delete=models.CASCADE)

class Order_details(models.Model):
    od_id = models.IntegerField(primary_key=True)
    o_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    unitprice = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.IntegerField(max_length=2)

class Cupon(models.Model):
    cupon_id = models.IntegerField(primary_key=True)
    s_id= models.ForeignKey(Salesman, on_delete=models.CASCADE)
    discount = models.IntegerField(max_length=2)
    cupon_use_number = models.IntegerField()
    cupon_max_use_number = models.IntegerField()

class Report(models.Model):
    report_id = models.IntegerField(primary_key=True)
    c_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    report_desc = models.CharField(max_length=100)
    report_type = models.CharField(max_length=100)
    report_date = models.DateTimeField()
    report_satatus = models.CharField(max_length=20)
    resolve_date = models.DateTimeField()
    