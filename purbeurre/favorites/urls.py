from django.urls import path
from . import views


app_name = "favorites"

urlpatterns = [
    path('', views.user_favorites, name="user_favorites"),
    path('show/', views.show_favorites, name="show_favorites"),
]
