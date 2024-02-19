from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('registration/', views.registration, name="registration"),
    path('log_out/', views.user_logout, name='user_logout')
] 