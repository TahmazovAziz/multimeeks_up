from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', all_view, name='administration'),
    path('update/<int:pk>/', UpdateMedia.as_view(),name='update'),
    path('create_media/', CreateMedia.as_view(),name='create_m'),
    path('create_episode/', CreateEpisode.as_view(), name='create_e')

]
    