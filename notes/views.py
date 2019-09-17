from django.shortcuts import render
from .models import Note
from django.contrib.auth.decorators import login_required
from users.models import UserProfile, User

@login_required
def notes(req):
    user_data = req.user
    notes = {'notes': Note.objects.all(), 'user_data': user_data}
    
    return render(req, 'notes/notes.html', context=notes)