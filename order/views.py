from django.shortcuts import render

def index(request):
    return render(request, 'order/index.html')

def order_list(request):
    return render(request, 'order/order_list.html')
