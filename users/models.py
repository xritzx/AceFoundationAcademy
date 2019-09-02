from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator, MaxLengthValidator

MAX_VAL = 10**16
MIN_VAL = 10**9
YEAR = []

def fetch_year():
    YEAR.clear()
    yr = datetime.now().year
    for r in range(yr-5, yr+5):
        YEAR.append((str(r),str(r)))
fetch_year()

#Model Class for more feature
class UserProfile(models.Model):

    user = models.OneToOneField(User)

    contact_number = models.IntegerField(validators=[MinValueValidator(MIN_VAL), MaxValueValidator(MAX_VAL)], blank=True, help_text="Optional Example: XXXXXXXXXX")
    guardian_name = models.CharField(max_length=40, help_text="Father/Mother/Gaurdian Name")
    contact_number_of_guardian = models.IntegerField(validators=[MinValueValidator(MIN_VAL), MaxValueValidator(MAX_VAL)], help_text="Required * Example: XXXXXXXXXX")
    address = models.TextField(blank=True, help_text="Optional")
    
    class_X_school_name = models.CharField(max_length=40, help_text="Enter your School Name", blank=True)
    class_X_board_name = models.CharField(max_length=6, choices=(("CBSE", "CBSE"), ("ICSE", "ICSE"), ("WBSE", "WBSE")), default="ICSE")
    class_X_year_of_passing = models.CharField(choices=YEAR, max_length=5)
    last_exam_marksheet = models.ImageField(upload_to="users/marksheet", blank=True, help_text="Marksheet should name as 'YOUR_NAME_CLASS' less than 200kB")

    profile_pic = models.ImageField(upload_to="users/profile_pic", blank=True, help_text="Image should be less than 200kB")


    def __str__(self):
        return self.user.first_name + " Username: " + self.user.username
