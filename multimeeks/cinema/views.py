from django.shortcuts import render
from cinema.models import Episode , Media  , Message
from django.views.generic import ListView , UpdateView
from django.views import View
# def player(request , media_slug , pk , room_name):
#     media = Episode.objects.all().select_related('media_id').filter(media_id=pk)
#     media_info = Media.objects.filter(id=pk)
#     coment_room = Message.objects.select_related('chatid')
#     context={
#         "media":media,
#         "room_name":room_name,
#         "coment_room":coment_room,
#         'media_info':media_info
#     }

#     return render(request,'cinema/player.html',context)

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
