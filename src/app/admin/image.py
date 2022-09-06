from django.contrib import admin
from app.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'created_at', 'last_update')
    list_filter = ('created_at', 'last_update')
    search_fields = ('image',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'last_update')


admin.site.register(Image, ImageAdmin)
