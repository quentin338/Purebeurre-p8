from django.shortcuts import render
from django.http import HttpResponse

from .forms import SearchForm
from .models import Product, Category


def index(request):
    return HttpResponse("TEST !")


def detail(request, product_id):
    return HttpResponse("Here is the product detail !")


def product_search(request):
    form = SearchForm(request.POST or None)

    if form.is_valid():
        user_search = form.cleaned_data['search']

        results = Product.objects.filter(name__icontains=user_search)

    return render(request, "products/home_test.html", locals())
