from django.db import models


class ProductManager(models.Manager):

    def search_autocomplete(self, user_search):
        # results = Product.objects.filter(name__icontains=user_search).order_by('-nutriscore')[:10]
        results = super().get_queryset().filter(name__icontains=user_search) \
                      .order_by('-nutriscore')[:10]

        results = [product.name for product in results]

        return results

    def get_better_products(self, user_search):
        # product_category = Product.objects.filter(name=user_search).first().category
        product_category = super().get_queryset().filter(name=user_search).first().category
        better_products = product_category.products.order_by('nutriscore')[:6]

        return better_products
