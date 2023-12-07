from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    adddvs = adddv.objects.all()
    context = {'adddvs': adddvs}
    return render(request,"app/home.html",context)
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'app/register.html',context)
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username =username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'user or password in correct!')
    
    context = {}
    return render(request,'app/login.html',context)
def themkh(request):
        
        addkhs = addkh.objects.all().order_by('id')
        context = {'addkhs':addkhs}
        return render(request,"app/add.html",context) 
def cart(request):
        adddvs = adddv.objects.all()
        context = {'adddvs': adddvs}
        return render(request,"app/cart.html",context)
def checkout(request):
        context = {}
        return render(request,"app/checkout.html")

         
    
    

