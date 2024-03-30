from django.http import JsonResponse
from django.shortcuts import redirect, render

from app.models import slider
from app.models import banner_area
from category.models import Category, Main_Category
from product.models import Product,Coupon_Code
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

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
       return render(request,'cart/checkout.html')