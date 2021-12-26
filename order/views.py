from django.shortcuts import render
from .models import Order

def index(request):
    return render(request, 'order/index.html')

def order_list(request):
    orders = Order.objects.all
    context = {'orders': orders}
    return render(request, 'order/order_list.html', context)
