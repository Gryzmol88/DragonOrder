from django.db import models

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
    product_price = models.IntegerField()
    transport_price = models.IntegerField()
    current_transport_price = models.CharField(max_length=3, choices=CURRENT_CHOICES, default='USD')
    customs_price = models.IntegerField()
    total_weight = models.IntegerField()

    class Meta:
        ordering = ('-date_of_order',)


    def __str__(self):
        return self.name
