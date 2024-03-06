from django.shortcuts import render
from .form import UserProfileForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def RegisterUser(request):
    # if request.method == 'POST':
    #     user_form = UserCreationForm(request.POST)
    #     profile_form = UserProfileForm(request.POST)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user = user_form.save()
    #         profile = profile_form.save(commit=False)
    #         profile.user = user
    #         profile.save()
    #         return redirect('login')
    # else:
    #     user_form = UserCreationForm()
    #     profile_form = UserProfileForm()
    # return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})
    
    
    # if not request.user.is_authenticated:
    #     if request.method == 'POST':
    #       register_form= UserProfileForm(request.POST)
    #       if register_form.is_valid():
    #          register_form.save()
    #          messages.success(request,'Account created successfully')
    #          return redirect('home')
       
    #     else:
    #           register_form= UserProfileForm()
    #     return render(request,'register.html',{'form': register_form})
    # else:
    #     return redirect('login')


     if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the data to the database
            return redirect('home')
     else:
        form = UserProfileForm()
     return render(request, 'register.html', {'form': form})


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
               user_name = form.cleaned_data['username']
               user_pass = form.cleaned_data['password']
               user = authenticate(username=user_name,password=user_pass)
               if user is not None:
                  messages.success(request,' logged in successfully')
                  login(request,user)
                  return redirect('home')
               else:
                messages.warning(request,'something went wrong')
                return redirect('register')
            
        else:
            form=AuthenticationForm()
        return render(request,'login.html',{'form':form,'type':"login"})
    else:
        return redirect('login')


@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')