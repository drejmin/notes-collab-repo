from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import Note

# Create your views here.
class NoteDetail(DetailView):
  model = Note