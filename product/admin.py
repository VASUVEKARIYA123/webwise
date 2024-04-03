from django.contrib import admin
from .models import *
from cart.cart import Cart
# Register your models here.

class Product_Images(admin.TabularInline):
    model = Product_Image

class Additional_Informations(admin.TabularInline):
    model = Additional_Information

class Product_admin(admin.ModelAdmin):
    inlines = (Product_Images,Additional_Informations)
    list_display=('product_name','price','categories','section')
    list_editable=('categories','section')




admin.site.register(Product,Product_admin)
admin.site.register(Product_Image)
admin.site.register(Section)
admin.site.register(Additional_Information)
admin.site.register(Coupon_Code)
