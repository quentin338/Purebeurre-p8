from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list_products"),
    path('<int:product_id>', views.detail, name="product_detail"),
]
