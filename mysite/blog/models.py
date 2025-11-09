
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):


    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts',null=False, blank=False)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT) 

    class Meta:      
        ordering = ['-publish']   # pour mettre les articles par ordre décroissant de date de publication  ' afficher les articles les plus récents en premier
        indexes=[
            models.Index(fields=['-publish']),  # index pour optimiser les requêtes de tri par date de publication
        ]

    def __str__(self):
        return self.title