from django.db import models
from djmoney.models.fields import MoneyField


class Order(models.Model):
    STATUS_CHOICES_ORDER = (
        ('W przygotowaniu', 'W przygotowaniu'),
        ('Zamówiono', 'Zamówiono'),
        ('Wysłano', 'Wysłano'),
        ('Dostarczono', 'Dostarczono'),
         )

    CURRENT_CHOICES = (
        ('PLN', 'PLN'),
        ('USD', 'USD'),
    )

    name = models.CharField(max_length=200)
    date_of_order = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES_ORDER, default='W przygotowaniu')
    product_price = MoneyField(max_digits=8, decimal_places=2, default_currency='USD')
    transport_price = MoneyField(max_digits=8, decimal_places=2, default_currency='USD')
    current_transport_price = MoneyField(max_digits=8, decimal_places=2, default_currency='USD')
    customs_price = MoneyField(max_digits=8, decimal_places=2, default_currency='USD')
    total_weight = models.IntegerField()

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
