from django.contrib import admin
from .models import Usuarios

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('user','totem','upload')
    list_filter = ('user','totem', 'upload')


    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Usuarios, UsuariosAdmin)
