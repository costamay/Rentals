from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


def index(request):
    return render(request, 'main/index.html')

@login_required(login_url='/accounts/login/?next=/')    
def houses(request):
    houses = House.objects.all
    return render(request,'main/houses.html', {'houses':houses})
    
@login_required(login_url='/accounts/login/?next=/')
def profile(request):
      current_user = request.user
      profile = Profile.objects.filter(user=current_user).first()
      
       
      return render(request, 'main/profile.html', { "profile": profile, 'current_user':current_user})

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

@login_required(login_url='/accounts/login/?next=/')
def details(request,id):
    house = House.objects.get(id=id)
    # owner = house.owner_set.all
    return render(request, 'main/details.html', {'house':house})


def search_results(request):
    if 'house' in request.GET and request.GET["house"]:
        search_term = request.GET.get("house")
        searched_houses = House.search(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{"message":message, "houses":searched_houses})

    else:
        messsage = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})