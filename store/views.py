from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def store(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        return render(request, 'store/index.html', {'products': products, 'customer': customer})
    return render(request, 'store/index.html', {'products': products})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #     empty cart to create if user is not logged in
        order = {'get_cart_total': 0, 'get_cart_total': 0}
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def user_login(request):
    return render(request, 'store/login_page.html')


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('login_page')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('store')
        )


def log_out_view(request):
    logout(request)
    return redirect('store')
