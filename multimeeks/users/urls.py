from django.contrib import admin
from django.urls import path , include
from .views import *
from rest_framework import routers
from .views import UsersViewset
router = routers.DefaultRouter()
router.register(r'users',UsersViewset)
urlpatterns = [
    path('users/' , include('django.contrib.auth.urls')),
    path('logout/' , LogoutView.as_view(), name="logout"),
    path('registration/',Register.as_view(), name='register'),
    path('api/' , include(router.urls))
]

urlpatterns+=router.urls