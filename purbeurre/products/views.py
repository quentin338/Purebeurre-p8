from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

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
        results = Product.search_autocomplete(user_search)

        return JsonResponse(results, safe=False)


def product_search(request):
    form = SearchForm(request.GET or None)

    if form.is_valid():
        user_search = form.cleaned_data['search']
        better_products = Product.get_better_products(user_search)

        return render(request, "products/results.html", {'better_products': better_products,
                                                         'user_search': user_search})

    redirect(request, "products:index")


def details(request, product_id):
    product = Product.objects.get(code=product_id)

    return render(request, "products/details.html", {'product': product})
