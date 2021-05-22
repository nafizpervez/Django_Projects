from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, ProfilePic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.views import View
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import Profiles

# Create your views here.
def signup(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(response, user)
            return redirect('lenus:index')
    else:
        form = RegistrationForm()
    return render(response, 'authentication/sign_up.html', {'form': form})



@login_required
def logout_request(request):
    auth.logout(request)
    return redirect('lenus:index')


@login_required
def profile(request):
    return render(request,'authentication/profile.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
                login(request,user)
                return redirect('lenus:index')
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'authentication/sign_up.html', {})


@login_required
def user_change(request):
    profile_form=Profiles(instance=request.user.users)
    if request.method == "POST":
        profile_form=Profiles(request.POST, request.FILES, instance=request.user.users)
        if profile_form.is_valid():
            form2=profile_form.save(commit=False)
            form2.save()
            return redirect('/profile')


    return render(request,'authentication/edit_profile.html',context={'profile_form':profile_form})



@login_required
def add_pro_pic(request):
    form=ProfilePic()
    if request.method=="POST":
        form=ProfilePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user=request.user
            user_obj.save()
            return redirect('/profile')


    return render(request,'authentication/add_pro_pic.html',context={'form':form})



@login_required
def change_pro_pic(request):
    form=ProfilePic(instance=request.user.users)
    if request.method=="POST":
        form=ProfilePic(request.POST,request.FILES,instance=request.user.users)
        if form.is_valid():
            form.save()
            return redirect('/profile')

    return render(request,'authentication/change_pro_pic.html',context={'form':form})
