from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    context = {"page_name": "HOME", "title": "Home"}
    return render(request, 'home/index.django-html', context)
