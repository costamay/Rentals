from django.shortcuts import render,redirect
from .models import *

def index(request):
    return render(request, 'main/index.html')

def profile(request):
      current_user = request.user
      profile = Profile.objects.filter(user=current_user).first()
      posts = request.user.post_set.all()
       
      return render(request, 'main/profile.html', {"posts": posts, "profile": profile, 'current_user':current_user})

def update_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        form =  ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
        return render(request,'main/update_profile.html', {'form':form})