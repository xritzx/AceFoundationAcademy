from django.shortcuts import render
from .models import Note
from django.contrib.auth.decorators import login_required

@login_required
def notes(req):
    notes = {'notes': Note.objects.all()}
    return render(req, 'notes/notes.html', context=notes)