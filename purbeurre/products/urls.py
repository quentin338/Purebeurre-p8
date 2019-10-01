from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('', views.product_search, name="product_search"),
    path('<int:product_id>', views.detail, name="product detail"),

]
