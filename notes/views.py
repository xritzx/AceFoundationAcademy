from django.shortcuts import render
from .models import Note

def notes(req):
    notes = {'notes': Note.objects.all()}
    return render(req, 'notes/notes.html', context=notes)