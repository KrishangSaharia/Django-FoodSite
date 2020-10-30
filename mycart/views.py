from django.shortcuts import render, redirect
from item.models import Item
from django.shortcuts import render

from .models import Cart, CartItem
from django.http import HttpResponse
from delivery.models import DeliveryBoy


def view_cart(request):
    cart_id=request.session.get('cart_id',None)
    user=request.user
    if user.is_authenticated:
        if cart_id is not None:
            cart_obj=Cart.objects.get(pk=cart_id)
            cartitems=CartItem.objects.filter(cart=cart_obj)
        else:
            cart_obj=Cart.objects.create(user=user)
            request.session['cart_id']=cart_obj.id
            cartitems=CartItem.objects.filter(cart=cart_obj)
        n=DeliveryBoy.objects.filter().count()
        deliverytime=15*(n+1)

        return render(request,'mycart/view.html',{'cartitems':cartitems,'deliverytime':deliverytime,'ordertotal':'0'})

    else:
        return HttpResponse("Please Go Back And LogIn First!!")

def checkout(request):
    cart_id=request.session.get('cart_id', None)
    user=request.user
    if user.is_authenticated:
        if cart_id is not None:
            cart_obj=Cart.objects.get(pk=cart_id)
            n=DeliveryBoy.objects.filter(is_active=True).count()
            deliverytime=15*(n+1)
            return render(request,'mycart/view.html',{'deliverytime':deliverytime,'ordertotal':'0'})


def add_cart(request,item_id):
    cart_id=request.session.get('cart_id',None)
    user=request.user
    if user.is_authenticated:
        if cart_id is None:
            cart_obj=Cart.objects.create(user=user)
            request.session['cart_id']=cart_obj.id
            cartitem=CartItem.objects.filter(user=user,item=Item.objects.get(pk=item_id))
            cartitems=cart_obj.items.all()
        else :
            cart_obj=Cart.objects.get(pk=cart_id)
            if CartItem.objects.filter(cart=cart_obj,item=Item.objects.get(pk=item_id)).exists():
                cartitem=CartItem.objects.get(cart=cart_obj,item=Item.objects.get(pk=item_id))
                cartitem.quantity+=1
                cartitem.save()
                cartitems=CartItem.objects.filter(cart=cart_obj)
            else:
                cartitem=CartItem.objects.create(cart=cart_obj,item=Item.objects.get(pk=item_id))
                cartitem.quantity=1
                cartitem.save()
                cartitems=CartItem.objects.filter(cart=cart_obj)
        return render(request,'mycart/view.html',{'cartitems':cartitems}) 
    else :
        return HttpResponse("Please Go Back and LOgin First!")
