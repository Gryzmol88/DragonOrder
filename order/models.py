from django.db import models

class Order(models.Model):
    STATUS_CHOICES = (
        ('W przygotowaniu', 'W przygotowaniu'),
        ('Zamówiono', 'Zamówiono'),
        ('Wysłano', 'Wysłano'),
        ('Dostarczono', 'Dostarczono'),
         )
    name = models.CharField(max_length=200)
    date_of_order = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='W przygotowaniu')
    product_price = models.IntegerField()
    transport_price = models.IntegerField()
    customs_price = models.IntegerField()
    total_weight = models.IntegerField()

    class Meta:
        ordering = ('-date_of_order',)


    def __str__(self):
        return self.name
