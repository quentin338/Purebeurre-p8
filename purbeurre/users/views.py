from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate

from .forms import UserForm


def profile(request):
    if request.user.is_authenticated:
        return HttpResponse('Ceci est un profil utilisateur')
    else:
        return redirect("user registration")


def user_login(request):
    form = UserForm(request.GET or None)

    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)

    return redirect("products:index")


def user_check_login(request):
    form = UserForm(request.GET or None)

    if form.is_valid():
        user_mail = form.cleaned_data['email']
        user_password = form.cleaned_data['password']

        user = authenticate(email=user_mail, password=user_password)

        if user:
            login(request, user)
        else:
            return redirect("users:user_login")

    return redirect(reverse("products:index"))


def create_new_user(request):
    pass
