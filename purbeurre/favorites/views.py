from django.shortcuts import render, redirect
from django.http import HttpResponse


def user_favorites(request):
    # if request.user.is_authenticated:
    return HttpResponse('User favorites !')

