from django.db import models
from django_countries.fields import CountryField
from django.core.validators import FileExtensionValidator

class Media(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    discription = models.TextField()
    direct_by = models.CharField(max_length=40)
    country = CountryField(multiple=True)
    poster = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True , null=True)
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")
    category =  models.ForeignKey('Category' , on_delete=models.PROTECT)
    def __str__(self):
        return self.name
    
class Episode(models.Model):
    ep_count = models.IntegerField()
    source = models.FileField(upload_to="video/%y" ,null=True,  blank=True,  validators=[FileExtensionValidator( ['mp4'] ) ])    
    media_id = models.ForeignKey('Media', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(unique=True, db_index=True) 

    def __str__(self):
        return self.name
    