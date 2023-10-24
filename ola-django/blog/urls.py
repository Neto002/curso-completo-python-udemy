from django.urls import path

from . import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.blog, name='home'),
    path('post/<int:id>/', blog_views.post, name='post'),
    path('articles/', blog_views.articles, name='articles')
]
