from django.contrib import admin
from .models import Course, Teachers, Gallery, About, Achievement, Feedback

class GalleryAdmin(admin.ModelAdmin):
    """The only Main class of Gallery Admin"""
    list_display = ('subject', 'date')
    list_filter = ('date', 'subject')

admin.site.register(Gallery, GalleryAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('your_name', 'email', 'date')
    list_filter=('date',)
    search_fields=('details',)

    class Meta:
        model= Feedback

admin.site.register(Feedback, FeedbackAdmin)

admin.site.register(Course)
admin.site.register(Teachers)
admin.site.register(About)
admin.site.register(Achievement)