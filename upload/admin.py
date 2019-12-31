from django.contrib import admin
from .models import Usuarios

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('user','totem','image_tag')
    list_filter = ('user','totem', 'upload')


admin.site.register(Usuarios, UsuariosAdmin)
