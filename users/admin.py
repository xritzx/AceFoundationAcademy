from django.contrib import admin
from .models import UserProfile
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ['contact_number', 'guardian_name', 'subjects', 'class_X_school_name', 'class_X_board_name', 'class_X_year_of_passing', 'last_exam_marksheet', 'profile_pic']
admin.site.register(UserProfile, UserAdmin)