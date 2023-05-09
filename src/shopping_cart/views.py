from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from permissions import permissions
from products.models import Product
from shopping_cart.models import Cart
from shopping_history.models import History

# Create your views here.

@login_required()
@permission_required(permissions.ECOMMERCE_CLIENT)
def Add_To_Cart(request, product_id):
    cart = Cart.objects.get(user=request.user.id)
    cart.products['products'].append(product_id)
    cart.save()
    return redirect('dashboard')

@login_required()
@permission_required(permissions.ECOMMERCE_CLIENT)
def View_Cart(request):
    context = {'products':[], 'total_price':0}
    cart = Cart.objects.get(user=request.user.id)
    for it in cart.products['products']:
        temp = Product.objects.get(pk=it)
        context['total_price'] += temp.price
        context['products'].append(temp)
    return render(request, 'shopping_cart/cart.html', context)

@login_required()
@permission_required(permissions.ECOMMERCE_CLIENT)
def Buy_Products(request):
    cart = Cart.objects.get(user=request.user.id)
    history = History.objects.get(user=request.user.id)
    history.history['history'].append(cart.products['products'])
    cart.products['products'] = []
    cart.save()
    history.save()
    return redirect('dashboard')
