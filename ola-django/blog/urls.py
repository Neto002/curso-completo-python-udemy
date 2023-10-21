from django.urls import path

from . import views as blog_views

urlpatterns = [
    path('', blog_views.blog),
    path('articles/', blog_views.articles)
]
