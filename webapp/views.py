from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse
import json, uuid


def index(request):
    latest_product_list = Product.objects.all()
    context = {
        'latest_product_list': latest_product_list,
    }
    return render(request, 'webapp/index.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'webapp/detail.html', {'product': product})


def sign_in(request):
    return render(request, 'webapp/sign_in.html')


def cart(request):
    return render(request, 'webapp/cart.html')


def menu(request):
    latest_product_list = Product.objects.all()
    context = {
        'latest_product_list': latest_product_list,
    }
    return render(request, 'webapp/menu.html', context)


def add_count(request):
    quantity = request.POST.get('nowCount')
    name = request.POST.get('name')
    cart_id = request.POST.get('cart_id')
    print('add_count:  ', quantity)
    print('add_name:  ', name)
    print('cart_id:  ', cart_id)
    data = {'result': 'true'}
    return HttpResponse(json.dumps(data))


def min_count(request):
    quantity = request.POST.get('nowCount')
    name = request.POST.get('name')
    cart_id = request.POST.get('cart_id')
    print('min_count:  ', quantity)
    print('min_name:  ', name)
    print('cart_id:  ', cart_id)
    data = {'result': 'true'}
    return HttpResponse(json.dumps(data))





