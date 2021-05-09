from django.contrib import admin
from django.urls import path, include
from zembo import views

urlpatterns = [
    path('',views.index, name="zembo"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutuser, name="logout"),

]
