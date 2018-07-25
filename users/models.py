from django.db import models
from django.contrib.auth.models import User

#Model Class for more feature
class UserProfile(models.Model):

    user = models.OneToOneField(User)
    board_name = models.CharField(max_length=6, choices=(("CBSE", "CBSE"), ("ICSE", "ICSE"), ("WBSE", "WBSE")))
    profile_pic = models.ImageField(upload_to = "users/profile_pic", blank=True)

    def __str__(self):
        return self.user.first_name
