from django.contrib import admin
from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') ## pour le tableau de bord admin
    list_filter = ('status', 'created', 'publish', 'author') ## pour ajouter des filtres latéraux dans l'interface d'administration interface dans la droite
    search_fields = ('title', 'body') ## pour ajouter une barre de recherche en haut de la page d'administration
    prepopulated_fields = {'slug': ('title',)} ## pour remplir automatiquement le champ slug en fonction du titre lors de la création d'un nouvel article par exemple  post de mortada djebbouri => post-de-mortada-djebbouri
    raw_id_fields = ('author',) ## pour utiliser un champ de recherche au lieu d'un menu déroulant pour les relations étrangères et par numero d'identification de l'auteur 
    date_hierarchy = 'publish' ## pour ajouter une hiérarchie de dates en haut de la page d'administration pour naviguer rapidement entre les articles publiés à différentes dates
    ordering = ( 'author','status', 'publish') ## pour définir l'ordre par défaut des articles dans l'interface d'administration, ici par auteur, puis par statut et enfin par date de publication