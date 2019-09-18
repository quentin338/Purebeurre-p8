from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("TEST !")


def detail(request, product_id):
    return HttpResponse("Here is the product detail !")
