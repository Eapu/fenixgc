from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import La_Cilla,Degollada_del_Humo,Acusa,Tejeda,Lugarejos,Las_Hoyas,Tamadaba,Pajaritos,Degollada_del_Sargento,Fin_del_Mundo,Cruz_de_Maria,Cuevas_del_Caballero,Fuentefria,Cueva_Corcho,Doña_Paca,Galaz

# Create your views here.

def index(request, tag_slug=None):
             posts = La_Cilla.published.all()
             posts9 = Fin_del_Mundo.published.all()
             posts4 = Tejeda.published.all()
             return render(request,'green/index.html',  {'posts': posts,'posts9': posts9,'posts4': posts4})
def indexmap(request, tag_slug=None):
             posts = La_Cilla.published.all()
             posts9 = Fin_del_Mundo.published.all()
             posts4 = Tejeda.published.all()
             return render(request,'green/mapa.html',  {'posts': posts,'posts9': posts9,'posts4': posts4})

def fenixgram(request, tag_slug=None):
             posts = La_Cilla.published.all()
             posts2 = Degollada_del_Humo.published.all()
             posts3 = Acusa.published.all()
             posts4 = Tejeda.published.all()
             posts5 = Lugarejos.published.all()
             posts6 = Las_Hoyas.published.all()
             posts7 = Tamadaba.published.all()
             posts8 = Degollada_del_Sargento.published.all() 
             posts9 = Fin_del_Mundo.published.all()
             posts10 = Cruz_de_Maria.published.all()
             posts11 = Cuevas_del_Caballero.published.all()
             posts12 = Fuentefria.published.all()
             posts13 = Cueva_Corcho.published.all()
             posts14 = Doña_Paca.published.all()
             posts15 = Galaz.published.all()
             posts16 = Pajaritos.published.all()



             return render(request,'green/fenixgram.html',  {'posts': posts,'posts2': posts2,'posts3': posts3,'posts4': posts4,'posts5': posts5,'posts6': posts6,'posts7': posts7,'posts8': posts8,'posts9': posts9,'posts10': posts10,'posts11': posts11,'posts12': posts12,'posts13': posts13,'posts14': posts14,'posts15': posts15,'posts16': posts16})


