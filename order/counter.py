from .models import Order, Product

def refresh_order():
    """Obliczanie nowych wartości po dodaniu przedmiotów do zamówienia"""
    orders = Order.objects.all()
    for order in orders:
        order_items(order)
        order_weight(order)
        order_products_price(order)
        transport_customs_price(order)


def order_items(order):
    """"Obliczanie ilości wszystkich przedmitów w zamówieniu"""
    products = Product.objects.filter(order=order.id)
    all_items = 0
    for product in products:
        all_items += product.quantity
    order.all_items = all_items
    order.save()

def order_weight(order):
    """"Obliczanie wagi całego zamówienia"""
    products = Product.objects.filter(order=order.id)
    total_weight = 0
    for product in products:
        all_items = product.quantity * product.weight
        total_weight += all_items
    order.total_weight = total_weight
    order.save()

def order_products_price(order):
    """"Obbliczanie całej wartości zamóweinia na podstawie cen poszczeólnych produktów"""
    products = Product.objects.filter(order=order.id)
    total_price = 0
    for product in products:
        all_items = product.quantity * product.purchase_row_price
        total_price += all_items
    order.product_price = total_price
    order.save()

def transport_customs_price(order):
    """"Obliczanie calkowitej wartości opłat dodatkowych (tranposrt plus cło)"""
    #Jeżeli transport jest w USD
    if order.transport_price.currency.code == 'USD':

        order.total_transport_price = order.customs_price + (order.transport_price * order.usd_price)
        order.save()
    #Jeżeli transport jest w PLN
    else:
        order.total_transport_price = order.customs_price + order.transport_price
        order.save()


