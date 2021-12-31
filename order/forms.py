from django import forms
from .models import Order, Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ['name', 'date_of_order', 'status', 'product_price',
                  'transport_price',
                  'customs_price', 'total_weight']

        labels = {
            'name': 'Nazwa zamówienia:',
            'date_of_order': 'Data zakupu',
            'status': 'Satus',
            'product_price': 'Cena produktów:',
            'transport_price': 'Cena transportu',
            'customs_price': 'Oplaty celne (VAT i cło)',
            'total_weight': 'całkowita waga [kg]',
        }

        widgets = {'date_of_order': forms.NumberInput(attrs={'type': 'date'})}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = ['product_name', 'weight', 'purchase_row_price',
                  'quantity', 'purchase_final_price']
        labels = {
            'product_name': 'Nazwa produktu',
            'weight': 'Waga',
            'purchase_row_price': 'Cena zakupu',
            'quantity': 'Ilość',
            'purchase_final_price': 'Ostateczna cena',
        }

