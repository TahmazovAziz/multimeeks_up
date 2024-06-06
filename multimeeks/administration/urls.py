from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('',  include('django.contrib.auth.urls')),
    path('main', all_view, name='administration'),
    path('update/<int:pk>/', UpdateMedia.as_view(),name='administration_update'),
    path('create_media/', CreateMedia.as_view(),name='administration_create_media'),
    path('create_episode/', CreateEpisode.as_view(), name='administration_create_episode')

]
    