from django.db import models


class FavoriteManager(models.Manager):

    def create_favorite(self, user, product_id):
        pass
