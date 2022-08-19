from django.contrib import admin
from Image.models import ImageFile

class ImageFile_admin(admin.ModelAdmin):
    # fields = ['name', 'date']
    search_fields = ['ImageFile']

admin.site.register(ImageFile, ImageFile_admin)


