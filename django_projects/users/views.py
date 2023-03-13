from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from .models import User
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm


def profile(request):
    if request.method == 'POST':
         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
         if form.is_valid():
            form.save()
            messages.success(request, "Успешно!")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)


def login(request):
    if request.method == 'POST':
         form = UserLoginForm(data=request.POST)
         if form.is_valid():
             username = request.POST['username']
             password = request.POST['password']
             user = auth.authenticate(username=username, password=password)
             if user:
                 auth.login(request, user)
                 messages.success(request, "Вы успешно авторизовались!")
                 return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались!")
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm
    context = {'form': form}
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
