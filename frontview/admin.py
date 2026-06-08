from django.contrib import admin
from .models import ConferencePresentation, FlagshipProject, Publications, Events, Video, GalleryImage

# Register your models here.

admin.site.register(FlagshipProject)
admin.site.register(Publications)
admin.site.register(Events)
admin.site.register(ConferencePresentation)
admin.site.register(Video)
admin.site.register(GalleryImage)
