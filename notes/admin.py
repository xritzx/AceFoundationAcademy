from django.contrib import admin
from .models import Note
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'publication_date')
    list_filter = ('subject', 'teacher', 'publication_date')

admin.site.register(Note, NoteAdmin)