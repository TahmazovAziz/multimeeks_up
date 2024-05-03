from django.shortcuts import render
from cinema.models import Episode , Media  , Message
def player(request , media_slug , pk , room_name):
    media = Episode.objects.all().select_related('media_id').filter(media_id=pk)
    media_info =  Media.objects.filter(id=pk)
    niknaim_data = Message.objects.all()
    coment_room = Message.objects.select_related('chatid')
    context={
        "media":media,
        "media_info":media_info,
        "room_name":room_name,
        "niknaim_data":niknaim_data,
        "coment_room":coment_room
    }

    return render(request,'cinema/player.html',context)

