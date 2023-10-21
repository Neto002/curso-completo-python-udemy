from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def blog(request: HttpRequest) -> HttpResponse:
    context = {"page_name": "BLOG", "title": "Blogs"}
    return render(request, "blog/index.html", context)


def articles(request: HttpRequest) -> HttpResponse:
    context = {"page_name": "ARTICLES", "title": "Articles"}
    return render(request, "blog/articles.html", context)
