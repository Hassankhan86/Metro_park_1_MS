from django.contrib import admin
from django.urls import path

from .import views
app_name = "accounts"

urlpatterns = [

    path('login', views.loginpage, name='login'),
    path('register', views.registerpage, name='register'),
    path('logout', views.logoutUser, name='logout'),

]
