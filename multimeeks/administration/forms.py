from  cinema.models import Media , Episode
from django.forms import ModelForm
from django.forms import ModelForm , TextInput ,DateTimeInput , Textarea
class MediaForm(ModelForm):
    class Meta:
        model = Media
        fields = '__all__'
class EpisodeForm(ModelForm):
    class Meta:
        model = Episode
        fields = '__all__'