from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .forms import SearchForm
from .models import Product, Category


def index(request):
    form = SearchForm(request.GET or None)

    # if form.is_valid():
    #     user_search = form.cleaned_data['search']
    #     return redirect("product_search", user_search=user_search)

    return render(request, "products/index.html", {'form': form})


def product_autocomplete(request):
    user_search = request.GET.get('term')

    if user_search is not None:
        results = Product.objects.search_autocomplete(user_search)

        return JsonResponse(results, safe=False)


def product_search(request):
    form = SearchForm(request.GET or None)

    if form.is_valid():
        user_search = form.cleaned_data['search']
        better_products = Product.objects.get_better_products(user_search)

        return render(request, "products/results.html", {'better_products': better_products,
                                                         'user_search': user_search})

    return redirect("products:index")


def details(request, product_id):
    try:
        product = Product.objects.get(code=product_id)
    except ObjectDoesNotExist:
        return redirect("products:index")

    return render(request, "products/details.html", {'product': product})
