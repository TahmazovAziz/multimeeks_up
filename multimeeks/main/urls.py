from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('' , main_page ,name='home_page'),
    path('<slug:cat_slug>/',ShowCategory.as_view())
]

