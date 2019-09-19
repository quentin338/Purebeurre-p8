from django.db import models


class Favorite(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    new_product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name="new_product")
    ancient_product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name="ancient_product")
