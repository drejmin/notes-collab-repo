from django.urls import path
from . import views

urlpatterns =[

    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='notes_detail'),


    path('', views.home, name= 'home')
    path('notes/', views.notes_on_notes_index, name='index'),



]