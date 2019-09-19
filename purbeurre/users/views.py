from django.shortcuts import render, redirect
from django.http import HttpResponse


def profile(request):
    if request.user.is_authenticated:
        return HttpResponse('Ceci est un profil utilisateur')
    else:
        return redirect("user registration")


def register(request):
    return HttpResponse('USER REGISTRATION')
