from django.shortcuts import render, get_object_or_404
from .models import Product, CartDetail
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
    cart_id = request.session.get('cart_id')
    latest_cart_list = CartDetail.objects.filter(cart_id=cart_id)

    cds = CartDetail.objects.filter(cart_id=cart_id).values()
    total = 0
    for cd in latest_cart_list:
        cd_total = cd.quantity * cd.product_id.price  # 购物车内某一种商品的总价
        total += cd_total
        print('cd_total:', cd_total)
        #print('total:', total)
    context = {
        'latest_cart_list': latest_cart_list,
        'total': total,
    }
    return render(request, 'webapp/cart.html', context)


def menu(request):
    latest_product_list = Product.objects.all()
    context = {
        'latest_product_list': latest_product_list,
    }
    return render(request, 'webapp/menu.html', context)


def alter_cd(quantity, product, cart_id):
    if quantity and product and cart_id:
        c_latest = CartDetail(quantity=quantity, product_id=product, cart_id=cart_id)
        if CartDetail.objects.filter(cart_id=cart_id, product_id=product):
            CartDetail.objects.filter(cart_id=cart_id, product_id=product).update(
                product_id=product, quantity=quantity)
            print('successfully updated')
        else:
            c_latest.save()
            print('successfully saved a new cart detail')
    else:
        print('error, null exists')


def add_count(request):
    quantity = request.POST.get('nowCount')
    name = request.POST.get('name')
    product = Product.objects.get(name=name)
    cart_id = request.POST.get('cart_id')
    alter_cd(quantity, product, cart_id)
    request.session['cart_id'] = cart_id
    print('add_count:  ', quantity)
    print('add_name:  ', name)
    print('cart_id:  ', cart_id)
    data = {'result': 'true'}
    return HttpResponse(json.dumps(data))


def min_count(request):
    quantity = request.POST.get('nowCount')
    name = request.POST.get('name')
    product = Product.objects.get(name=name)
    cart_id = request.POST.get('cart_id')
    alter_cd(quantity, product, cart_id)
    print('min_count:  ', quantity)
    print('min_name:  ', name)
    print('cart_id:  ', cart_id)
    data = {'result': 'true'}
    return HttpResponse(json.dumps(data))





