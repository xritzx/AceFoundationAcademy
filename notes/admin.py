from django.contrib import admin
from .models import Note
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('topic','subject', 'teacher', 'publication_date', 'for_class')
    list_filter = ('topic','subject', 'teacher', 'publication_date', 'for_class')

admin.site.register(Note, NoteAdmin)