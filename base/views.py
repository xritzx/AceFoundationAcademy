from django.shortcuts import render
from .models import Course,Teachers,Gallery,About,Achievement
# Create your views here.
def index(req):
    
    contents={}

    # Course setup
    course=Course.objects.all()
    contents['course']=course

    # Gallery
    gallery=Gallery.objects.all()
    contents['gallery']=gallery

    #About
    about=About.objects.all()
    contents['about']=about

    # Teachers
    teachers=Teachers.objects.all()
    contents['teachers']=teachers
    
    #Achievements
    achievements=Achievement.objects.all()
    contents['achievements']=achievements

    return(render(
        req,'base/base.html',context=contents
    ))