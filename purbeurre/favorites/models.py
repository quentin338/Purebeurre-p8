from django.db import models
from django.conf import settings


class Favorite(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    new_product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name="new_product")
    ancient_product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name="ancient_product")
