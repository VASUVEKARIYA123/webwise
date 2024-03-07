from django.contrib import admin

from .models import User,Bank_details,Personal_info,Address,Customer,Salesman,Product,images,Wishlist,Wishlist_products,Review,Cart,Cart_products,Shipper,Payment,Order,Order_details,Cupon,Report

# Register your models here.
admin.site.register(User)
admin.site.register(Bank_details)
admin.site.register(Personal_info)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Salesman)
admin.site.register(Product)
admin.site.register(images)
admin.site.register(Wishlist)
admin.site.register(Wishlist_products)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(Cart_products)
admin.site.register(Shipper)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(Order_details)
admin.site.register(Cupon)
admin.site.register(Report)




