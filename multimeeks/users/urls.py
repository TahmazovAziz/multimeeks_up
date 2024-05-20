from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('users/' , include('django.contrib.auth.urls')),
    path('logout/' , LogoutView.as_view(), name="logout"),
    path('registration/',Register.as_view(), name='register')
]

