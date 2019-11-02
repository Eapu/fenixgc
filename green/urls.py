from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from .views import fenixgram
from django.conf import settings
from django.conf.urls.static import static

app_name = 'green'

urlpatterns = [
  	url(r'^$', views.index, name='index'),
	url(r'^fenixgram/', views.fenixgram, name='fenixgram'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
