from django.shortcuts import render, redirect, get_object_or_404
from shop_app.models import Products
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quandity < cart_item.product.stock:
            cart_item.quandity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quandity=1, cart=cart)
        cart_item.save()
    return redirect('cart_app:cart_details')


def cart_details(request, counter=0, total=0, cart_items=None, ):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, active=True)
    try:
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quandity)
            counter += cart_item.quandity
    except Products.DoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter, ))


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quandity > 1:
        cart_item.quandity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_app:cart_details')


def remove_all(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_app:cart_details')
