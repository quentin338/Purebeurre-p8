import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Favorite


def user_favorites(request):
    if request.user.is_authenticated:
        # print(request.POST)
        old_product_code = request.POST.get('old_product')
        new_product_code = request.POST.get('new_product')
        print(old_product_code)
        print(new_product_code)
        print(request.user)

        # Favorite.objects.create(old_product=old_product_code,
        #                         new_product=new_product_code,
        #                         user=request.user)

        return JsonResponse({"key": "value"})

