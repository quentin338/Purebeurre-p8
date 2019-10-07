from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path('', views.profile, name="user_profile"),
    path('new/', views.create_new_user, name="user_registration"),
    path('login/', views.user_login, name="user_login"),
    path('login/check/', views.user_check_login, name="user_check_login"),
    path('logout/', views.user_logout, name="user_logout")
]
