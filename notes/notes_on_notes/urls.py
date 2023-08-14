from django.urls import path
from . import views

urlpatterns =[

    path('', views.home, name= 'home')
    path('notes/', views.notes_on_notes_index, name='index'),


]