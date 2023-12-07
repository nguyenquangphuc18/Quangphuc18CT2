from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.register, name="register"),
    path("login/",views.loginPage, name="login"),
    path("add/",views.themkh, name="add"),
    path("cart/",views.cart, name="cart"),
    path("checkout/",views.checkout, name="checkout"),  
   
]
urlpatterns +=static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
