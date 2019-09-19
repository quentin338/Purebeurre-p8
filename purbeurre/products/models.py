from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    image_url = models.CharField(max_length=200)
    nutriscore = models.SmallIntegerField()
    ingredients_image = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
