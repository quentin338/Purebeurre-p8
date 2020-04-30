import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Favorite
from products.models import Product


def user_favorites(request):
    if request.user.is_authenticated:
        # print(request.POST)
        ancient_product_code = request.POST.get('old_product_code')
        new_product_code = request.POST.get('new_product_code')

        ancient_product = Product.objects.get(code=ancient_product_code)
        new_product = Product.objects.get(code=new_product_code)

        Favorite.objects.create_favorite(ancient_product=ancient_product,
                                         new_product=new_product,
                                         user=request.user)

        return JsonResponse({"key": "value"})

