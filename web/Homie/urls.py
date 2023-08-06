from django.contrib import admin
from django.urls import path,include
from Homie import views

urlpatterns = [
     path('',views.home,name='home'),
     path('login',views.loginUser,name='login'),
     path('contact',views.contact,name='contact'),
     path('logout',views.logoutUser,name='logout'),
     path('inside',views.inside,name='inside')

]


