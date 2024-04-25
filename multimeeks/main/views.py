from django.shortcuts import render
from cinema.models import Media, Category
from django.shortcuts import get_object_or_404

def main_page(request):
    media = Media.objects.all()
    context = {
        "media":media,
    }
    return render(request ,'main/main.html' , context)

def show_category(request,cat_slug):
    category = get_object_or_404(Category , slug=cat_slug)
    media = Media.objects.filter(category=category.pk)
    
    context = {
        "media":media
    }
    return render(request ,'main/main.html' , context)