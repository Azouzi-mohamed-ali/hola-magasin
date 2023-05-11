from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib import messages
from magasin.forms import ProduitForm,FournisseurForm,CommandeForm,UserRegistrationForm
from .models import Produit,Fournisseur,Commande
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer
class CategoryAPIView(APIView):
 def get(self, *args, **kwargs):
   categories = Categorie.objects.all()
   serializer = CategorySerializer(categories, many=True)
   return Response(serializer.data)
def aaa(request):
    template=loader.get_template('magasin/mesProduits.html')
    products= Produit.objects.all()
    context={'products':products}
    return render( request,'magasin/mesProduits.html',context )

    
@login_required
def index(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm()
        list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list,'form':form})

@login_required
def nouveauProduit(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm()
        list=Produit.objects.all()
    return render(request,'magasin/majProduits.html',{'list':list,'form':form})

@login_required
def listFournisseur(request):
    if request.method == "POST" : 
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/nouvFournisseur')
    else :
        form = FournisseurForm()
        list=Fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'list':list,'form':form})

@login_required
def nouveauFournisseur(request):
    if request.method == "POST" : 
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/nouvFournisseur')
    else :
        form = FournisseurForm()
        list=Fournisseur.objects.all()
    return render(request,'magasin/ajoutFournisseur.html',{'list':list,'form':form})


@login_required
def nouveauCommande(request):
    if request.method == "POST" : 
        form = CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/nouvFournisseur')
    else :
        form = CommandeForm()
        list=Commande.objects.all()
    return render(request,'magasin/fournisseur.html',{'list':list,'form':form})

def register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return HttpResponseRedirect('/magasin')
    else :
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form' : form})


