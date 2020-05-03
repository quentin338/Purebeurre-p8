from django.db import models
from django.db.utils import IntegrityError


class FavoriteManager(models.Manager):
    def create_favorite(self, **kwargs):
        try:
            self.create(**kwargs)
        except IntegrityError as e:
            print(e)
            pass

    def is_favorite(self, user, ancient_product, new_product):
        return bool(self.filter(user=user, ancient_product=ancient_product,
                                new_product=new_product))
