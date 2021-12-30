from django.shortcuts import render, redirect
from .models import Order, Product
from .forms import OrderForm, ProductForm
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

def new_order(request):
    if request.method != 'POST':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order:order_list')
    context = {'form': form}
    return render(request, 'order/new_order.html', context)

def new_product(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method != 'POST':
        form = ProductForm()
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
           new_product = form.save(commit=False)
           new_product.order = order
           new_product.save()
           return redirect('order:order_products', order_id=order_id)

    context = {'order': order, 'form': form}
    return render(request, 'order/new_product.html', context)

def edit_order(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method != 'POST':
        form = OrderForm(instance=order)
    else:
        form = OrderForm(instance=order, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('order:order_list')

    context = {'order': order, 'form': form}
    return render(request, 'order/edit_order.html', context)

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    context = {'order': order}
    return render(request, 'order/delete_order.html', context)

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    order_products = product.order

    if request.method != 'POST':
        form = ProductForm(instance=product)
    else:
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('order:order_products', order_id=order_products.id)

    context = {'product': product, 'form': form, 'order_products': order_products}
    return render(request, 'order/edit_product.html', context)

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    order_products = product.order
    product.delete()
    context = {'product': product, 'order_products': order_products}
    return render(request, 'order/delete_product.html', context)
