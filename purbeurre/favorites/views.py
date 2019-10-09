import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_favorites(request):
    if request.user.is_authenticated:
        # print(request.POST)
        code_product = request.POST.get('product')
        print(code_product)
        print(request.user)
        return JsonResponse({"key": "value"})

