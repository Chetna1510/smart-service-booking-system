from django.shortcuts import render

# Create your views here.


def provider_register(request):
    return render(request, "providers/register.html")
