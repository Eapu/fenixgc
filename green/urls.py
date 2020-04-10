from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from .views import fenixgram, indexmap
from django.conf import settings
from django.conf.urls.static import static

app_name = 'green'

urlpatterns = [
  	url(r'^$', views.index, name='index'),
  	url(r'^mapa/', views.indexmap, name='indexmap'),
	url(r'^fenixgram/', views.fenixgram, name='fenixgram'),
	url(r'^fenixgram/', views.fenixgram, name='fenixgram'),
	url(r'^privacidad/', views.privacidad, name='privacidad'),
	url(r'^cookies/', views.cookies, name='cookies'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
