from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .forms import SearchForm
from .models import Product, Category


def index(request):
    form = SearchForm(request.POST or None)

    if form.is_valid():
        user_search = form.cleaned_data['search']

    return render(request, "products/index.html", locals())


def detail(request, product_id):
    return HttpResponse("Here is the product detail !")


def product_search(request):
    user_search = request.GET.get('term')
    print(user_search)

    if user_search is not None:
        results = Product.search_products(user_search)

        return JsonResponse(results, safe=False)
