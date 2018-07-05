from datetime import datetime
from django.db import models
from stdimage import StdImageField

departments=(
        ('Physics','Physics'),
        ('Chemistry','Chemistry'),
        ('Mathematics','Mathematics'),
        ('Biology','Biology'),
        ('Computer','Computer'),
        ('Others','Others'),
    )

# Create your models here.

class Course(models.Model):
    types=(('cogs','Engineering'),('stethoscope','Medical'),('graduation-cap','Foundation Course'))
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
    image=StdImageField(upload_to='static/base/img/team',variations={'thumbnail':(250,250,True)})
    def __str__(self):
        return(str(self.name))

class Gallery(models.Model):
    subjects=departments
    image=StdImageField(upload_to='static/base/img/gallery',variations={'thumbnail':(1200,720,True)})
    subject=models.CharField(max_length=20,choices=subjects,default='Mathematics')
    descriptions=models.CharField(max_length=500)
    date=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return("Image of {} class".format(str(self.subject)))

class About(models.Model):
    title=models.CharField(max_length=300)
    detail=models.CharField(max_length=1200)
    
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

    def __str__(self):
        return self.your_name