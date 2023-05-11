
from django.db import models
from datetime import date
# Create your models here.
class Categorie(models.Model):
    name=models.CharField(max_length=50,default='Al')
    def __str__(self):
        return self.name


class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.nom+" "+self.adresse+" "+self.email+" "+self.telephone

class Produit(models.Model):
    TYPE_CHOICES=[('em','emballé'),('fr','Frais'),('cs','Conserve')]
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='Non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)
    catégorie=models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True)
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.libellé+" "+self.description+" "+str(self.prix)

class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return self.Duree_garantie+" "+self.libellé

class ProduitC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return self.Duree_garantie+" "+self.libellé

class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def __str__(self):
        return str(self.dateCde)+" "+str(self.totalCde)