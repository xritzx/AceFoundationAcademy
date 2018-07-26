from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator, MaxLengthValidator


#Model Class for more feature
class UserProfile(models.Model):

    user = models.OneToOneField(User)

    contact_number = models.IntegerField(validators=[MinLengthValidator(10), MaxLengthValidator(15)], blank=True, help_text="Optional")
    guardian_name = models.CharField(max_length=40, help_text="Father/Mother/Gaurdian Name")
    contact_number_of_guardian = models.IntegerField(validators=[MinLengthValidator(10), MaxLengthValidator(15)], help_text="Required *")
    address = models.TextField(blank=True, help_text="Optional")
    fresher_or_dropper = models.CharField(max_length=10, help_text="Enter wheather a Fresher or not", choices=(('Fresher', 'Fresher'),('Dropper', 'Dropper')), default="Fresher")
    
    class_X_school_name = models.CharField(max_length=40, help_text="Enter your School Name", blank=True)
    class_X_board_name = models.CharField(max_length=6, choices=(("CBSE", "CBSE"), ("ICSE", "ICSE"), ("WBSE", "WBSE")), default="ICSE")
    class_X_year_of_passing = models.DateField()
    class_X_marksheet = models.ImageField(upload_to="users/marksheetX", blank=True)
    class_X_percentage = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(40)], default=40)
    subjects_opted = models.CharField(max_length=5, choices=(("PCMB", "PCMB"), ("PCM", "PCM"), ("PCB", "PCB")), default="PCB", help_text="P: Physics, C: Chemistry, M: Mathematics, B: Biology")

    class_XII_board_name = models.CharField(max_length=6, choices=(("CBSE", "CBSE"), ("ICSE", "ICSE"), ("WBSE", "WBSE")), default="CBSE", help_text="Optional, Only in case of dropper", blank=True)
    class_XII_year_of_passing_or_expected = models.DateField(blank=True, help_text="Optional, Only in case of dropper")
    class_XII_marksheet = models.ImageField(upload_to="users/marksheetXII", blank=True, help_text="Optional, Only in case of dropper")
    class_XII_percentage = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(30)], help_text="Optional, Only in case of dropper", blank=True, default=40)

    profile_pic = models.ImageField(upload_to="users/profile_pic", blank=True)


    def __str__(self):
        return self.user.first_name+" Username: "+self.user.username
