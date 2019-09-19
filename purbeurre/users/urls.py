from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="user profile"),
    path('new/', views.register, name="user registration")
]
