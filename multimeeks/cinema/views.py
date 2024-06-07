from django.shortcuts import render
from cinema.models import Episode , Media  , Message
from django.views.generic import ListView , UpdateView
from django.views import View
from rest_framework import viewsets
from .serializers import *

class Player(ListView):
    model = Episode
    template_name = 'cinema/player.html'
    context_object_name = 'media'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media'] = Episode.objects.all().select_related('media_id').filter(media_id=self.kwargs['pk'])
        context['room_name'] = self.kwargs['room_name']
        context['media_info']= Media.objects.filter(id=self.kwargs['pk'])
        context['coment_room'] = Message.objects.select_related('chatid')
        return context

class MediaViewset(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializers

class EpisodeViewset(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializers
