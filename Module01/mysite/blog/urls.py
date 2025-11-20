
from django.contrib import admin
from django.urls import path

from . import views

#blog/url.py
app_name = 'blog' 
urlpatterns = [
    #path('', views.home, name='home'),

    #path('about/', views.about, name='about'),
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),

    
]



