"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from products.views import Products, UpdateProduct, DeleteProduct
from dashboard.views import Dashboard
from shopping_cart.views import Add_To_Cart, View_Cart, Buy_Products
from signup.views import User_Signup, Staff_Signup
from logout.views import Logout
from shopping_history.views import View_History

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),

    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name = 'login'),
    path('user_signup/', User_Signup, name = 'user_signup'),
    path('staff_signup/', Staff_Signup, name = 'staff_signup'),
    path('logout/', Logout, name = 'logout'),

    path('', Dashboard, name = 'dashboard'),

    path('shopping_cart/', View_Cart, name = 'cart'),
    path('add/shopping_cart/<int:product_id>', Add_To_Cart, name = 'add_to_cart'),
    path('buy_products/', Buy_Products, name = 'buy'),
    path('shopping_history/', View_History, name = 'history'),

    path('products/', Products, name = 'products'),
    path('products/update/<int:product_id>/', UpdateProduct, name = 'update_product'),
    path('products/delete/<int:product_id>/', DeleteProduct, name = 'delete_product')
]
