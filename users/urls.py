from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('sign_in/', views.user_sign, name="user_sign")
] 