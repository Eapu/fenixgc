from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = 'Fenix Gran Canaria'                    # default: "Django Administration"
admin.site.index_title = 'Fenix'                 # default: "Site administration"
admin.site.site_title = 'Fenix' # default: "Django site admin"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('green.urls')),
    url(r'^', include('upload.urls')),
    url(r'^', include('blog.urls')),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
