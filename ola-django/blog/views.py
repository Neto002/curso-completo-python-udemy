from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def blog(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/index.html')


def articles(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/articles.html')
