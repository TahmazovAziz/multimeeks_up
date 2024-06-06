from django.contrib import admin
from django.urls import path , include
from .views import *
from rest_framework import routers
from cinema.views import *
router = routers.DefaultRouter()
router.register(r'media', MediaViewset)
router.register(r'episode', EpisodeViewset)

urlpatterns = [
    path('api/',include(router.urls)),
    path('' , main_page ,name='home_page'),
    path('<slug:cat_slug>/',ShowCategory.as_view())

]
urlpatterns+=router.urls


