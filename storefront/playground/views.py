from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F, Value, Q
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
from .tasks import notify_customers


def say_hello(request):
    notify_customers.delay("testing")
    return render(request, 'hello.html', {'name': 'Oskar'})

    # queryset = Product.objects.filter(price__range=(20, 30))
    # queryset = Product.objects.filter(title__icontains='coffee')
