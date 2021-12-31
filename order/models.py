from django.db import models
from djmoney.models.fields import MoneyField



class Order(models.Model):
    STATUS_CHOICES_ORDER = (
        ('W przygotowaniu', 'W przygotowaniu'),
        ('Zamówiono', 'Zamówiono'),
        ('Wysłano', 'Wysłano'),
        ('Dostarczono', 'Dostarczono'),
         )


    name = models.CharField(max_length=200)
    date_of_order = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES_ORDER, default='W przygotowaniu')
    #Koszt wszystkich produktow w USD
    product_price = MoneyField(max_digits=8, decimal_places=2, default_currency='USD')
    #Koszt samego transportu w PLN lub USD
    transport_price = MoneyField(max_digits=8, decimal_places=2, default_currency='USD')
    #Całkowita waga zamówienia
    total_weight = models.FloatField()
    #Całkowita ilość produktów.
    all_items = models.IntegerField(default=0)
    #Koszt transportu i cła
    total_transport_price = MoneyField(max_digits=8, decimal_places=2, default_currency='PLN', default=0)
    #Koszt opłat celnych
    customs_price = MoneyField(max_digits=8, decimal_places=2, default_currency='PLN', default=0)
    #opłaty dodatkowe za kg w PLN
    fee_per_kg = MoneyField(max_digits=8, decimal_places=2, default_currency='PLN', default=0)
    #Całkowity koszt z oplatami w PLN
    total_price = MoneyField(max_digits=8, decimal_places=2, default_currency='PLN', default=0)

    class Meta:
        ordering = ('-date_of_order',)


    def __str__(self):
        return self.name

class Product(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    weight = models.IntegerField()
    purchase_row_price = MoneyField(max_digits=8, decimal_places=2, default_currency='USD')
    quantity = models.IntegerField()
    purchase_final_price = MoneyField(max_digits=8, decimal_places=2, default_currency='PLN')

    def __str__(self):
        return self.product_name
