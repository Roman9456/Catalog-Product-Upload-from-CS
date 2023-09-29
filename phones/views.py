from django.shortcuts import render
from phones.models import Phone

def phone_catalog(request):
    sort_param = request.GET.get('sort')
    phones = Phone.objects.all()

    if sort_param == 'name':
        phones = phones.order_by('name')
    elif sort_param == 'min_price':
        phones = phones.order_by('price')
    elif sort_param == 'max_price':
        phones = phones.order_by('-price')

    return render(request, 'phones/catalog.html', {'phones': phones})

def phone_detail(request, slug):
    phone = Phone.objects.get(slug=slug)
    return render(request, 'phones/product.html', {'phone': phone})

def home(request):
    return render(request, 'phones/home.html')