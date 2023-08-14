from django.shortcuts import render, redirect
from .models import Note



# Create your views here.
def notes_on_notes_index(request):
  notes = Note.objects.all()
  return render(request, 'notes_on_notes/index.html', {
    'notes': note
  })


