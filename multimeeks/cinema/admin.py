from django.contrib import admin
from cinema.models import Media,Episode,Category,ComentName,Message ,Niknaim


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
class MediaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
admin.site.register(Media, MediaAdmin)
admin.site.register(Episode)
admin.site.register(Category,CategoryAdmin)
admin.site.register(ComentName)
admin.site.register(Message)
admin.site.register(Niknaim)

