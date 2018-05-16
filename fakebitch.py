import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Firstapp.settings')
import django
django.setup()
import random
from users.models import User
from faker import Faker

fakegen=Faker()
# topics=['Sexy','bitch','nigga','trans','lesbo']

# def add_topic():
#      t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#      t.save()
#      return(t)

def populate(n=8):
    for i in range(n):
        
        fake_fname=fakegen.first_name()
        fake_lname=fakegen.last_name()
        fake_email=fakegen.email()
        users=User.objects.get_or_create(fname=fake_fname,lname=fake_lname,email=fake_email)[0]

if __name__ =='__main__':
    print("NoW populating bich")
    populate(n=100)


        