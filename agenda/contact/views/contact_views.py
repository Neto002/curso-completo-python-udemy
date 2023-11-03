from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from contact.models import Contact

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.filter(show=True).order_by('-id')

    context = {
        'contacts': contacts
    }

    return render(request, 'contact/index.html', context=context)


def contact(request: HttpRequest, contact_id) -> HttpResponse:
    single_contact = get_object_or_404(Contact, id=contact_id, show=True)

    context = {
        'contact': single_contact
    }

    return render(request, 'contact/contact.html', context=context)
