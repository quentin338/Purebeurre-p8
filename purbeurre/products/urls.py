from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/<str:user_search>', views.product_search, name="product search"),
    path('autocomplete/', views.product_autocomplete, name="product autocomplete"),
    path('<int:product_id>', views.detail, name="product detail"),
]
