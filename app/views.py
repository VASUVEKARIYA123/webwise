import math
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render
import razorpay


from app.models import slider
from app.models import banner_area
from category.models import Category, Main_Category
from order.models import AddressAndInfo, Order, OrderItem
from product.models import Product,Coupon_Code
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from razorpay.client import Client
from django.views.decorators.csrf import csrf_exempt


client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))

from django.template.loader import render_to_string
from django.db.models import Max , Min , Sum


# Create your views here.
def index(request):
        sliders = slider.objects.all().order_by('-id')[0:3]
        banner_areas = banner_area.objects.all().order_by('-id')[0:3]

        main_category = Main_Category.objects.all().order_by('-id')
        product = Product.objects.filter(section__name="Top Deals Of The Day")
        context = {
                'sliders' : sliders,
                'banner_areas' : banner_areas,
                'main_category' : main_category,
                'product' : product
        }
        return render(request,'main/index.html',context)

def PRODUCT_DETAILS(request,slug):
        product = Product.objects.filter(slug=slug)
        if product.exists() :
                product = Product.objects.get(slug=slug)
        else :
                return redirect('404')
        context = {
                        'product' : product
                  }
        return render(request,'product/product_details.html',context)

def Error404(request):
        return render(request,'errors/404.html')

def MY_ACCOUNT(request):
        return render(request,'account/myaccount.html')

def REGISTER(request):
        if request.method  == 'POST':
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')

                if User.objects.filter(username = username).exists():
                        messages.error(request,"username is already exists")
                        return redirect('login')
                if User.objects.filter(email = email).exists():
                        messages.error(request,"email is already exists")
                        return redirect('login')

                user = User(
                        username = username,
                        email = email,
                )
                user.set_password(password)
                user.save()
                return redirect('login')

        return None

def LOGIN(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request,username = username,password = password)
                if user is not None:
                        login(request,user)
                        return redirect('index')
                else:
                        messages.error(request,'Email And Password Are Invalid !')
                        return redirect('login')
@login_required(login_url='/accounts/login/')
def PROFILE(request):
        return render(request,'profile/profile.html')

def PROFILE_UPDATE(request):

        if request.method == 'POST':
                username = request.POST.get('username')
                last_name = request.POST.get('last_name')
                first_name = request.POST.get('first_name')
                email = request.POST.get('email')
                password = request.POST.get('password')
                user_id = request.user.id

                user = User.objects.get(id=user_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username=username
                user.email=email

                if password != None and password !="":
                        user.set_password(password)
                user.save()
        
        messages.success(request,'Profile Are Successfully Updated !')
        return redirect('profile')

def LOGOUT(request):
    logout(request)
    return redirect('index')

def ABOUT(request):
        return render(request,'main/about.html')

def CONTACT(request):
        return render(request,'main/contact.html')

def PRODUCT(request):
        category = Category.objects.all().order_by('-id')
        product = Product.objects.all()
        context = {
                'category' : category,
                'product' : product
        }
        return render(request,'product/product.html',context)
        
def filter_data(request):
    filter_params = request.GET
    filtered_products = Product.objects.filter(**filter_params)
    dta = {'product' : list(filtered_products.values())}
    return JsonResponse(dta)
#     categories = request.GET.getlist('category[]')
#     print("11111")
# #     brands = request.GET.getlist('brand[]')

#     allProducts = Product.objects.all().order_by('-id').distinct()
#     print(allProducts)
#     if len(categories) > 0:
#         allProducts = allProducts.filter(Categories__id__in=categories).distinct()

# #     if len(brands) > 0:
# #         allProducts = allProducts.filter(Brand__id__in=brands).distinct()


#     t = render_to_string('ajax/product.html', {'product': allProducts})

#     return JsonResponse({'data': t})


def CART(request):
        return render(request,'cart/cart.html')

@login_required(login_url='/accounts/login/')
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url='/accounts/login/')
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url='/accounts/login/')
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url='/accounts/login/')
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url='/accounts/login/')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url='/accounts/login/')
def cart_detail(request):
    cart = request.session.get('cart')
    packing_cost = sum(i['packing_cost'] for i in cart.values() if i)
    tax = sum(i['tax']*i['price']/100 for i in cart.values() if i)
    coupon = None
    valid_coupon = None
    invalid_coupon = None
    if request.method == 'GET':
           coupon_code = request.GET.get('coupon_code')
           if coupon_code :
                  try:
                       coupon = Coupon_Code.objects.get(code = coupon_code)
                       valid_coupon = "Are Applicable On Current Order !" 
                       cart_total_amount = cart.cart_total_amount ; 
                  except:
                         invalid_coupon = "Invalid Coupon Code !"
    context = { 
           'packing_cost':packing_cost,
           'tax':tax,
           'coupon' : coupon,
           'valid_coupon' : valid_coupon,
           'invalid_coupon' : invalid_coupon
    }
    return render(request, 'cart/cart.html',context)

def CHECKOUT(request):
       cart = request.session.get('cart')
       packing_cost = sum(i['packing_cost'] for i in cart.values() if i)
       tax =math.floor( sum(i['tax']*i['price']/100 for i in cart.values() if i))
       coupon = None
       valid_coupon = None
       invalid_coupon = None
       payment = client.order.create({
              "amount":500,
              "currency":"INR",
              "payment_capture":"1"
       })
       order_id = payment['id']

       
       context = { 
                'packing_cost':packing_cost,
                'tax':tax,
                'coupon' : coupon,
                'valid_coupon' : valid_coupon,
                'invalid_coupon' : invalid_coupon,
                'order_id' : order_id,
                'payment' : payment
        }
       return render(request,'cart/checkout.html',context)

def PLACE_ORDER(request):
       if request.method == 'POST':
                uid = request.session.get('_auth_user_id')
                user = User.objects.get(id = uid)
                address = request.POST.get('street_address')
                city = request.POST.get('city')
                stat = request.POST.get('state')
                postalcode = request.POST.get('postalcode')
                phone = request.POST.get('phone')
                order_id = request.POST.get('order_id')
                payment = request.POST.get('payment')
                cart_total_amount = request.POST.get('cart_total_amount')
                packing_cost = request.POST.get('packing_cost')
                delivery_cost = request.POST.get('delivery_cost')
                tax = request.POST.get('tax')
                total = request.POST.get('total')
                cart = request.session.get('cart')

                addressAndInfo = AddressAndInfo(
                       country = stat,
                       city = city,
                       addre = address,
                       phone = phone,
                       postalcode = postalcode,
                       user = user,
                )
                addressAndInfo.save()

                order = Order(
                       user = user,
                       packing_cost = packing_cost,
                       tax = tax,
                       delivery_charge = delivery_cost,
                       total = total,
                       payment_id = order_id,
                       address = addressAndInfo,
                )
                order.save()

                for i in cart : 
                        a = (int(cart[i]['price']))
                        b = cart[i]['quantity']
                        total = a*b
                        print(order)
                        print(total)
                        item = OrderItem(
                                order = order,
                                Product_id = cart[i]['product_id'],
                                quantity = cart[i]['quantity'],
                                price = cart[i]['price'],
                                total = total
                        )
                        item.save()
                

                        context = { 
                                'order_id' : order_id,
                                
                        }


       return render(request,'cart/success.html',context)

@csrf_exempt
def SUCCESS(request):
       if request.method == "POST":
              print('*************************')
              print('aaaaaaaaaaaaaaaaaaaaaaa')
              print('*************************')
              a = request.POST
              order_id = ""

              for key, val in a.items():
                     if key == 'razorpay_order_id':
                            order_id = val
                            break
              user = Order.objects.filter(payment_id = order_id).first()
              user.paid = True
              user.save()
                            
       return redirect('success1')

@csrf_exempt
def SUCCESS1(request):
       return render(request,'cart/success1.html')

       