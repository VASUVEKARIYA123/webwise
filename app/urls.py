from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index,name="index"),
    path('product/<slug:slug>',views.PRODUCT_DETAILS,name='product_details'),
    path('404',views.Error404,name='404'),

    path('about',views.ABOUT,name='about'),
    path('contact',views.CONTACT,name='contact'),
    path('product',views.PRODUCT,name='product'),
    path('product/filter-data',views.filter_data,name="filter-data"),
    

    # account url
    path('account/my-account',views.MY_ACCOUNT,name='my_account'),
    path('account/register',views.REGISTER,name='handleregister'),
    path('account/login',views.LOGIN,name='handlelogin'),
    path('account/logout',views.LOGOUT,name='handlelogout'),
    path('account/profile',views.PROFILE,name='profile'),
    path('account/profile/update',views.PROFILE_UPDATE,name='profile_update'),

    #cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/checkout',views.CHECKOUT,name='checkout'),
    path('cart/checkout/placeorder',views.PLACE_ORDER,name='placeorder'),
    path('cart/checkout/success',views.SUCCESS,name='success'),
    path('cart/checkout/successpage',views.SUCCESS1,name='success1'),

    path('accounts/',include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)