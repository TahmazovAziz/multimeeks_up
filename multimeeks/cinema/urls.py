from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('<int:pk>-<slug:media_slug>/<str:room_name>' , views.player,name='player'),
]

