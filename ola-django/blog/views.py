from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.data import posts

# Create your views here.


def blog(request: HttpRequest) -> HttpResponse:
    context = {"page_name": "BLOG", "title": "Blogs", 'posts': posts}
    return render(request, "blog/index.django-html", context)


def post(request: HttpRequest, id) -> HttpResponse:
    found_post = None

    for post in posts:
        if post['id'] == id:
            found_post = post
            break

    context = {'posts': [found_post]}
    return render(request, "blog/index.django-html", context)


def articles(request: HttpRequest) -> HttpResponse:
    context = {"page_name": "ARTICLES", "title": "Articles"}
    return render(request, "blog/articles.django-html", context)
