from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="list products"),
    path('', views.product_search, name="product search"),
    path('<int:product_id>', views.detail, name="product detail"),

]
