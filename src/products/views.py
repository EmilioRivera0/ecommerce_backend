from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

from permissions import permissions
from .models import Product, ProductForm

# Create your views here.
@login_required()
@permission_required(permissions.ECOMMERCE_STAFF)
def Products(request):
    if request.method == 'GET':
        form = ProductForm()
        context = {'products':list(Product.objects.all()), 'form':form}
        return render(request, 'products/products.html', context)
    
    elif request.method == 'POST':
        post_form = ProductForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('products')
        else:
            print(post_form.errors)
            return HttpResponseBadRequest('Incorrect Input Data')
        return render(request, 'products/products.html', {'form':post_form})

@login_required()
@permission_required(permissions.ECOMMERCE_STAFF)
def UpdateProduct(request, product_id):
    if request.method == 'GET':
        form = ProductForm(instance=Product.objects.get(pk=product_id))
        context = {'form':form, 'id':product_id}
        return render(request, 'products/update.html', context)
    elif request.method == 'POST':
        form = ProductForm(request.POST, instance=Product.objects.get(pk=product_id))
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print(form.errors)
            return HttpResponseBadRequest('Incorrect Input Data')
        return render(request, 'products/products.html', {'form':form})

@login_required()
@permission_required(permissions.ECOMMERCE_STAFF)
def DeleteProduct(request, product_id):
    Product.objects.filter(id = product_id).delete()
    return redirect('products')
