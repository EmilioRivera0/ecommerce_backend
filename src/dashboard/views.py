from django.shortcuts import render, redirect

from products.models import Product

# Create your views here.

def Dashboard(request):
    if request.method == 'GET':
        context = {'products':list(Product.objects.all())}
        return render(request, 'dashboard/dashboard.html', context)
