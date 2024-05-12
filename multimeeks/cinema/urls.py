from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path('<int:pk>-<slug:media_slug>/<str:room_name>' , Player.as_view(),name='player'),
]

