from django.db.models.query import QuerySet
from django.shortcuts import render
from cinema.models import Media, Category
from django.shortcuts import get_object_or_404
from django.views.generic import ListView 
def main_page(request):
    media = Media.objects.all()
    context = {
        "media":media,
    }
    return render(request ,'main/main.html' , context)


class ShowCategory(ListView):
    model = Media
    template_name = 'main/main.html'
    context_object_name = 'media'

    def get_queryset(self):
        category = get_object_or_404(Category , slug=self.kwargs['cat_slug'])
        return Media.objects.filter(category=category.pk)

