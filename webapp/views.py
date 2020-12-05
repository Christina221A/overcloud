from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Product

# Create your views here.
def index(request):
    latest_product_list = Product.objects.all()
    context = {
        'latest_product_list': latest_product_list,
    }
    return render(request, 'webapp/index.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'webapp/detail.html', {'product': product})

def signIn(request):
    return render(request, 'webapp/signIn.html')