from django.shortcuts import render
from cinema.models import Episode , Media 
def player(request , media_slug , pk):
    media = Episode.objects.all().select_related('media_id').filter(media_id=pk)
    media_info =  Media.objects.filter(id=pk)

    context={
        "media":media,
        "media_info":media_info,
    }

    return render(request,'cinema/player.html',context)