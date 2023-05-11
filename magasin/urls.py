from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CategoryAPIView

from . import views
urlpatterns = [ 
    path('', views.index, name='index'),
    path('neveauProduit/', views.nouveauProduit, name='ajoutProduit'),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
   
    path('listFournisseur/',views.listFournisseur,name='listFour'),
    path('nouvCommande/',views.nouveauCommande,name='nouveauCommande'),

    
    path('register/',views.register, name = 'register'),
     path('api/category/', CategoryAPIView.as_view())

]