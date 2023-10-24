from django.urls import path

from contact import views as contact_views

app_name = 'contact'

urlpatterns = [
    path('', contact_views.index, name='index'),
]
