from django.db import models
from products.models import Product


class Favorite(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
