from django.urls import path
from .views import user_register

urlpatterns = [
    path("register/user/", user_register, name="user_register"),

]
