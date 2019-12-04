from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from .views import create,created
from django.conf import settings
from django.conf.urls.static import static

app_name = 'upload' 
 
urlpatterns = [
	url(r'^create', views.create, name='create'),
	url(r'^created', views.created, name='created'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

