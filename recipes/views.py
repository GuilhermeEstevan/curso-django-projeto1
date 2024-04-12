from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "recipes/home.html", context={"name": "Guilherme Estevan"})


def about(request):
    return HttpResponse("Sobre")


def contact(request):
    return HttpResponse("Contato")
