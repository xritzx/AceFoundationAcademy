from django.contrib import admin
from .models import Course,Teachers,Gallery,About,Achievement
# Register your models here.
admin.site.register(Course)
admin.site.register(Teachers)
admin.site.register(Gallery)
admin.site.register(About)
admin.site.register(Achievement)