from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login

from signup.forms import Signup_Form
from shopping_cart.models import Cart
from shopping_history.models import History

# Create your views here.
def User_Signup(request):
    if request.method == 'GET':
        form = Signup_Form()
        print(Cart.objects.all())

    elif request.method == 'POST':
        form = Signup_Form(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user = User.objects.create(username=form.cleaned_data['username'], password=make_password(form.cleaned_data['password']), email=form.cleaned_data['email'])
                new_user.groups.add(Group.objects.get(name='Ecommerce_Clients'))
                Cart.objects.create(user=new_user, products = {'products':[]})
                History.objects.create(user=new_user, history={'history':[]})
                login(request, new_user)
                return redirect('dashboard')
            else:
                form.password = None
                form.password_check = None
        else:
            return HttpResponseBadRequest('Incorrect Input Data')

    return render(request, 'signup/user_signup.html', {'form':form})

def Staff_Signup(request):
    if request.method == 'GET':
        form = Signup_Form()
        print(Cart.objects.all())

    elif request.method == 'POST':
        form = Signup_Form(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user = User.objects.create(username=form.cleaned_data['username'], password=make_password(form.cleaned_data['password']), email=form.cleaned_data['email'], is_staff=True)
                new_user.groups.add(Group.objects.get(name='Ecommerce_Staff'))
                login(request, new_user)
                return redirect('dashboard')
            else:
                form.password = None
                form.password_check = None
        else:
            return HttpResponseBadRequest('Incorrect Input Data')

    return render(request, 'signup/staff_signup.html', {'form':form})
