import os
import json

from django.test import TestCase

from products.models import Product, Category


class ProductModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        path = os.path.dirname(os.path.abspath(__file__))
        sample_file = os.path.join(path, "sample_data", "sample1.json")

        with open(sample_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        cat = Category.objects.create(name="Charcuterie")
        for product in data['products']:
            product['category'] = cat
            Product.objects.create(**product)

    def setUp(self) -> None:
        self.best_prod = Product.objects.get(code=12345)

    def test_retrieving_product_nutriscore_img(self):
        self.assertEqual("nutriscore_a.png", self.best_prod.nutriscore_img)

    def test_retrieving_product_bad_nutriscore_img(self):
        prod_bad = Product.objects.get(code=54321)
        self.assertEqual("nutriscore_d.png", prod_bad.nutriscore_img)

    def test_retrieving_product_nutriscore_full_img(self):
        self.assertEqual("nutriscore_full_a.svg", self.best_prod.nutriscore_full_img)

    def test_retrieving_product_bad_nutriscore_full_img(self):
        prod_bad = Product.objects.get(code=54321)
        self.assertEqual("nutriscore_full_d.svg", prod_bad.nutriscore_full_img)

    def test_retrieving_product_url(self):
        self.assertEqual(f"https://fr.openfoodfacts.org/produit/12345", self.best_prod.url)

    # ProductManager
    def test_search_autocomplete_ten_products(self):
        self.assertEqual(10, len(Product.objects.search_autocomplete("Sauciss")))

    def test_search_autocomplete_order_by_nutriscore_desc(self):
        products = Product.objects.search_autocomplete("Sauciss")
        worst_prod = Product.objects.get(code=98765)
        self.assertEqual(worst_prod.name, products[0], msg="The first product is not the worst")

    def test_better_products_first_six(self):
        products = Product.objects.get_better_products("Saucisson sec")
        self.assertEqual(6, len(products))

    def test_better_products_best_product_first(self):
        products = Product.objects.get_better_products("Saucisson sec")
        self.assertEqual(self.best_prod.code, products[0].code)
