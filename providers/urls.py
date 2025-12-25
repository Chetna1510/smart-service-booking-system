from django.urls import path
from .views import provider_register

urlpatterns = [
    path("register/provider/", provider_register, name="provider_register"),

]
