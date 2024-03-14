from core.models import AddressAndInfo, Profile
from django.http import HttpResponse
from django.shortcuts import redirect, render


def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'core/unauthorized.html')
        return wrapper_func
    return decorator

def profile_exists(view_func):
    def wrapper_func(request, *args, **kwargs):
        if Profile.objects.filter(user = request.user):
            return render(request, 'core/unauthorized.html')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def address_exists(view_func):
    def wrapper_func(request, *args, **kwargs):
        if AddressAndInfo.objects.filter(user = request.user):
            return render(request, 'core/unauthorized.html')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func