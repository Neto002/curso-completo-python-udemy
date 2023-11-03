from django.urls import path

from contact import views as contact_views

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', contact_views.contact,  # type: ignore
         name='contact'),
    path('search/', contact_views.search, name='search'),  # type: ignore
    path('', contact_views.index, name='index'),  # type: ignore
]
