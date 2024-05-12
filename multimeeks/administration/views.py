from django.shortcuts import render
from cinema.models import Episode , Media  , Message
from django.views.generic import ListView , UpdateView , CreateView
from django.views import View
from django.urls import reverse_lazy
from .forms import MediaForm , EpisodeForm

def all_view(request):
    episodes = Episode.objects.all().select_related('media_id')
    media = Media.objects.all()
    context = {
        "episodes":episodes,
        "media_p":media,
    }
    return render(request, 'administration/all_view.html' , context)


class UpdateMedia(UpdateView):
    model = Media
    template_name ='administration/create.html'
    form_class = MediaForm
    EpisodeForm

class CreateMedia(CreateView):
    model = Media
    template_name ='administration/create.html'
    form_class = MediaForm
    success_url = reverse_lazy('create_e')
    

class CreateEpisode(CreateView):
    model = Episode
    template_name = 'administration/create.html'
    form_class = EpisodeForm
    success_url = reverse_lazy('home_page')