from rest_framework import serializers
from .models import *
from django_countries.serializers import CountryFieldMixin
class MediaSerializers(CountryFieldMixin,serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class EpisodeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'

