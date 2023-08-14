from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import Note


# Create your views here.

class NoteDetail(DetailView):
  model = Note

def notes_on_notes_index(request):
  notes = Note.objects.all()
  return render(request, 'notes_on_notes/index.html', {
    'notes': note
  })



