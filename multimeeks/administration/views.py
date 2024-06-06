from django.shortcuts import render , redirect
from cinema.models import Episode , Media  , Message
from django.views.generic import ListView , UpdateView , CreateView
from django.views import View
from django.urls import reverse_lazy
from .forms import MediaForm , EpisodeForm
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin

def all_view(request):
    episodes = Episode.objects.all().select_related('media_id')
    media = Media.objects.all()
    context = {
        "episodes":episodes,
        "media_p":media,
    }
    return render(request, 'administration/all_view.html' , context)


class UpdateMedia(PermissionRequiredMixin,UpdateView):
    model = Media
    template_name ='administration/create.html'
    form_class = MediaForm
    permission_required = 'administration.add_media'

class CreateMedia(PermissionRequiredMixin,CreateView):
    model = Media
    template_name ='administration/create.html'
    form_class = MediaForm
    success_url = reverse_lazy('create_e')
    permission_required = 'administration.add_media'


class CreateEpisode(PermissionRequiredMixin,CreateView):
    model = Episode
    template_name = 'administration/create.html'
    form_class = EpisodeForm
    success_url = reverse_lazy('home_page')
    permission_required = 'administration.add_media'
