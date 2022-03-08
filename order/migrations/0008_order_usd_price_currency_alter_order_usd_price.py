# Generated by Django 4.0 on 2022-01-02 20:30

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_order_usd_price_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='usd_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='usd_price',
            field=djmoney.models.fields.MoneyField(currency_choices=[('PLN', 'PLN')], decimal_places=2, default=Decimal('0'), max_digits=8),
        ),
    ]