from datetime import datetime
from django.db import models
from stdimage import StdImageField

departments=(
        ('Physics','Physics'),
        ('Chemistry','Chemistry'),
        ('Mathematics','Mathematics'),
        ('Biology','Biology'),
        ('Computer Sc.','Computer Sc.'),
        ('History/Geography','History/Geography'),
        ('Second Language', 'Second Language'),
        ('Others','Others'),
    )

# Create your models here.

class Course(models.Model):
    types=(('cogs','Gear Icon'),('stethoscope','Medic Icon'),('graduation-cap','Foundation Course'))
    Type=models.CharField(max_length=15,choices=types,default='cogs')
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=1200)
    def __str__(self):
        return("Course name is: {} ".format(str(self.name)))


class Teachers(models.Model):
    depts=departments
    name=models.CharField(max_length=50)
    dept=models.CharField(max_length=20,choices=depts,default='Mathematics')
    details=models.CharField(max_length=1000)
    image= models.URLField(max_length=200, help_text="Please Enter the URL here(GDrive/Amazon Drive/Facebook)")

    class Meta:
        verbose_name_plural="Faculty"
    
    def __str__(self):
        return(str(self.name))


class Gallery(models.Model):
    subjects=departments
    image= models.URLField(max_length=200, help_text="Please Enter the URL to photo here (GDrive/Amazon Drive/Facebook)")
    subject=models.CharField(max_length=20,choices=subjects,default='Mathematics')
    descriptions=models.CharField(max_length=500)
    date=models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural="Gallery"

    def __str__(self):
        return("Image of {} class".format(str(self.subject)))

class About(models.Model):
    title=models.CharField(max_length=300)
    detail=models.CharField(max_length=1200)

    class Meta:
        verbose_name_plural="About"

    def __str__(self):
        return("About: {}".format(str(self.title)))

class Achievement(models.Model):
    title=models.CharField(max_length=300)
    no=models.IntegerField(default=0)

    def __str__(self):
        return("Achievement "+str(self.title))

class Feedback(models.Model):

    your_name = models.CharField(max_length=120)
    email = models.EmailField()
    details = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Feedback"

    def __str__(self):
        return self.your_name