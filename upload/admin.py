from django.contrib import admin
from .models import Usuarios

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('user','totem','image_tag','uploaded_at')
    list_filter = ('user','totem', 'upload','uploaded_at')

    def thumbnail(self, obj):
        return format_html('<img src="{}" style="width: 130px; \
                           height: 100px"/>'.format(obj.url_image))

    thumbnail.short_description = 'thumbnail'

admin.site.register(Usuarios, UsuariosAdmin)
