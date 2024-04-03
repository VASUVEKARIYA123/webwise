from django.contrib import admin

from order.models import *

class OrderItems(admin.TabularInline):
    model=OrderItem

class Orderadmin(admin.ModelAdmin):
    inlines = [OrderItems] 
    
# Register your models here.
admin.site.register(AddressAndInfo)
admin.site.register(Order,Orderadmin)