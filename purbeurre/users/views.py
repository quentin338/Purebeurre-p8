from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.db.utils import IntegrityError

from .forms import UserForm
from .models import User


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
    form = UserForm(request.POST or None)

    return render(request, "users/registration.html", {'form': form})


def add_new_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        user_mail = form.cleaned_data['email']
        user_password = form.cleaned_data['password']

        try:
            user = User.objects.create_user(email=user_mail, password=user_password)
            return redirect("users:user_login")
        except IntegrityError as e:
            print(e)
            pass

    return redirect("users:user_registration")


def user_account(request):
    if request.user.is_authenticated:
        return render(request, "users/account.html")

    return redirect("users:user_login")
