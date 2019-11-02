from django.contrib import admin
from .models import La_Cilla,Degollada_del_Humo,Acusa,Tejeda,Lugarejos,Las_Hoyas,Tamadaba,Degollada_del_Sargento,Fin_del_Mundo,Cruz_de_Maria,Cuevas_del_Caballero,Fuentefria,Cueva_Corcho,Doña_Paca,Galaz,Pajaritos
from django.utils.html import format_html

# Register your models here.



class La_CillaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(La_Cilla, La_CillaAdmin)


class Degollada_del_HumoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Degollada_del_Humo, Degollada_del_HumoAdmin)



class AcusaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Acusa, AcusaAdmin)

class TejedaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Tejeda, TejedaAdmin)
class LugarejosAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Lugarejos, LugarejosAdmin)
class Las_HoyasAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Las_Hoyas, Las_HoyasAdmin)
class TamadabaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Tamadaba, TamadabaAdmin)

class Degollada_del_SargentoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Degollada_del_Sargento, Degollada_del_SargentoAdmin)

class Fin_del_MundoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Fin_del_Mundo, Fin_del_MundoAdmin)

class Cruz_de_MariaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Cruz_de_Maria, Cruz_de_MariaAdmin)
class Cuevas_del_CaballeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Cuevas_del_Caballero, Cuevas_del_CaballeroAdmin)

class FuentefriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Fuentefria, FuentefriaAdmin)

class Cueva_CorchoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Cueva_Corcho, Cueva_CorchoAdmin)

class Doña_PacaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Doña_Paca, Doña_PacaAdmin)

class GalazAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Galaz, GalazAdmin)
class PajaritosAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
admin.site.register(Pajaritos, PajaritosAdmin)
