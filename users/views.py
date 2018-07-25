from django.shortcuts import render
from .forms import UserForm, UserProfileForm

def register(req):
    registered = False
    if(req.method == "POST"):
        user_form = UserForm(data=req.POST)
        profile_form = UserProfileForm(data=req.POST)

        if(user_form.is_valid() and profile_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save() #Saving the Instant User Values

            profile = profile_form.save(commit=False)
            profile.user = user #Fetching Value into one to on field
            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
        
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(req, 'users/register.html', {'registered':registered,
                                                 'user_form':user_form,
                                                    'profile_form':profile_form})

def login(req):
    return render(req, 'users/login.html')