from .models import Order, Product

def refresh_order():
    """Obliczanie nowych wartości po dodaniu przedmiotów do zamówienia"""
    orders = Order.objects.all()
    for order in orders:
        order_items(order)
        order_weight(order)
        order_products_price(order)
        transport_customs_price(order)
        calculate_fee_per_kg(order)
        calculate_total_price(order)
        calculate_purchase_final_price(order)



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

        order.total_transport_price = order.customs_price.amount + (order.transport_price.amount * order.usd_price.amount)
        order.total_transport_price.currency.code = 'PLN'
        order.save()
    #Jeżeli transport jest w PLN
    else:
        order.total_transport_price = order.customs_price.amount + order.transport_price.amount
        order.total_transport_price.currency.code = 'PLN'
        order.save()

def calculate_fee_per_kg(order):
    """Obliczenie opłat dodatkwoych za kg towaru w PLN"""
    if order.total_weight > 0:
        order.fee_per_kg = order.total_transport_price/order.total_weight
        order.save()

def calculate_total_price(order):
    """Obliczanie całkowitej ceny zamówienia w PLN"""
    # Koszt wszystkich produktow w USD * Koszt wymiant z USD na PLN + Koszt transportu i cła
    order.total_price = (order.product_price.amount * order.usd_price.amount) + order.total_transport_price.amount
    order.total_price.currency.code = 'PLN'
    order.save()

def calculate_purchase_final_price(order):
    """Obliczenie ceny ostatecznej produktu w PLN"""
    products = Product.objects.filter(order=order.id)
    for product in products:
        #OPŁATY DODATKOWE ZA KG * WAGA PRODUKTU + CENA PRODUKTU * KURS WYMIANY WALUTY
        extra_fee_per_kg = product.weight * order.fee_per_kg.amount
        product_price_pln = product.purchase_row_price.amount * order.usd_price.amount
        product.purchase_final_price = extra_fee_per_kg + product_price_pln
        product.purchase_final_price.currency.code = 'PLN'
        product.save()
