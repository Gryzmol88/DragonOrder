from django.shortcuts import render
from .models import Order, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'order/index.html')

def order_list(request):
    object_list = Order.objects.all()
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    context = {'orders': orders, 'page': page}
    return render(request, 'order/order_list.html', context)

def order_products(request, order_id):
    order_products = Order.objects.get(id=order_id)
    products = Product.objects.filter(order=order_id)
    context = {'order_products': order_products, 'products': products}
    return render(request, 'order/order_products.html', context)
