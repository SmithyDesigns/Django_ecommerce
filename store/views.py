from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def store(request):
    """ This is a view that is rendering the store page. It is also checking if the user is authenticated. If the user
    is authenticated, it will render the store page with the customer information. If the user is not authenticated, it
    will render the store page without the customer information."""
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        return render(request, 'store/index.html', {'products': products, 'customer': customer})
    return render(request, 'store/index.html', {'products': products})


def cart(request):
    """ This is checking if the user is authenticated. If the user is authenticated, it will get the customer
     information and the order information. If the user is not authenticated, it will create an empty cart.
    (Else)This is creating an empty cart if the user is not authenticated."""
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
    """ This is checking if the user is authenticated. If the user is authenticated, it will get the customer
    information and the order information. If the user is not authenticated, it will create an empty cart.
    (else)empty cart to create if user is not logged in"""
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        order = {'get_cart_total': 0, 'get_cart_total': 0}
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def user_login(request):
    """
    When the user visits the login page, render the login_page.html template.

    :param request: The request is an HttpRequest object
    :return: The login page is being returned.
    """
    return render(request, 'store/login_page.html')


def authenticate_user(request):
    """ This is checking if the user is authenticated. If the user is authenticated, it will get the customer
    information and the order information. If the user is not authenticated, it will create an empty cart."""
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
    """
    It logs out the user and redirects them to the store page

    :param request: The request is an HttpRequest object
    :return: The logout function is being called on the request object.
    """
    logout(request)
    return redirect('store')
