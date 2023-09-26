from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone

def index(request):
    return redirect('catalog')


def phone_catalog(request):
    phones = Phone.objects.all()
    return render(request, 'catalog/catalog.html', {'phones': phones})

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'catalog/phone_detail.html', {'phone': phone})