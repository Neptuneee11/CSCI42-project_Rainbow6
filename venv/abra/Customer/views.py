from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserForm, ProfileForm

# Create your views here.

def create_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)  # Log in the user automatically
            return redirect('profile_page.html')
    
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'create_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def profile_page(request):
    profile = request.user.profile
    return render(request, 'profile_page.html', {
        'profile': profile,
    })
