from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from contact.models import Contact

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts
    }

    return render(request, 'contact/index.html', context=context)
