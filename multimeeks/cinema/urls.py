from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('<int:pk>-<slug:media_slug>' , views.player,name='player'),
]

