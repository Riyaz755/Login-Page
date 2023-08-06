from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime 
from Homie.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.

def home(request):
    print(request.user)
    if request.user.is_anonymous: 
     return redirect('/login')
    else:
       return redirect('/inside')

def loginUser(request):
    if request.method == 'POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        print(username,password)

        user=authenticate(username=username,password=password)

        if user is not None :
            login(request, user)
            return redirect("/inside")
        else:
          return render(request,'login.html')
    return render(request,'login.html')

def contact(request):
    if request.method == "POST":
        Name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        contact=Contact(name=Name,mobile=mobile,email=email,date=datetime.today())
        contact.save()
        messages.success(request,"Thank you your request has been submitted")

    return render(request,'contact.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def inside(request):
   return render(request,'inside.html')
