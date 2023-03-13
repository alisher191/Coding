from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')


def products(request):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products.html', context)


