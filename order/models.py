from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.

# User Profile Model
class AddressAndInfo(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    addre = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    postalcode = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    packing_cost = models.IntegerField()
    tax = models.IntegerField()
    delivery_charge = models.IntegerField()
    total = models.IntegerField() 
    payment_id = models.CharField(max_length=100,null=True,blank=True)
    paid = models.BooleanField(default=False,null=True)
    address = models.ForeignKey(AddressAndInfo,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
       
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price =models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.order.user.username
