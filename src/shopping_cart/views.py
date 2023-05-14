from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from datetime import datetime

from permissions import permissions
from products.models import Product
from shopping_cart.models import Cart
from shopping_history.models import History

# Create your views here.

@login_required()
@permission_required(permissions.ECOMMERCE_CLIENT)
def Add_To_Cart(request, product_id):
    cart = Cart.objects.get(user=request.user.id)
    temp_product = Product.objects.get(pk=product_id)
    temp_tuple = [temp_product.name, temp_product.brand.name, temp_product.price.to_eng_string()]
    cart.products['products'].append(temp_tuple)
    cart.save()
    return redirect('dashboard')

@login_required()
@permission_required(permissions.ECOMMERCE_CLIENT)
def View_Cart(request):
    context = {'products':[], 'total_price':0}
    cart = Cart.objects.get(user=request.user.id)
    for it in cart.products['products']:
        context['total_price'] += float(it[2])
        context['products'].append(it)
    return render(request, 'shopping_cart/cart.html', context)

@login_required()
@permission_required(permissions.ECOMMERCE_CLIENT)
def Buy_Products(request):
    cart = Cart.objects.get(user=request.user.id)
    for it in cart.products['products']:
        it.append(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    history = History.objects.get(user=request.user.id)
    history.history['history'].extend(cart.products['products'])
    cart.products['products'] = []
    cart.save()
    history.save()
    return redirect('dashboard')
