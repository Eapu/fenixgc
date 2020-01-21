from django.contrib import admin
from .models import Usuarios

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('user','totem','image_tag','uploaded_at')
    list_filter = ('user','totem', 'upload','uploaded_at')


admin.site.register(Usuarios, UsuariosAdmin)
