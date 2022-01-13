# Generated by Django 4.0 on 2022-01-02 19:56

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_customs_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customs_price',
            field=djmoney.models.fields.MoneyField(currency_choices=[('PLN', 'PLN')], decimal_places=2, default=Decimal('0'), max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='customs_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='fee_per_kg',
            field=djmoney.models.fields.MoneyField(currency_choices=[('PLN', 'PLN')], decimal_places=2, default=Decimal('0'), max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='fee_per_kg_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_price',
            field=djmoney.models.fields.MoneyField(currency_choices=[('USD', 'USD $')], decimal_places=2, default=Decimal('0'), max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=djmoney.models.fields.MoneyField(currency_choices=[('PLN', 'PLN')], decimal_places=2, default=Decimal('0'), max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_transport_price',
            field=djmoney.models.fields.MoneyField(currency_choices=[('PLN', 'PLN')], decimal_places=2, default=Decimal('0'), max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_transport_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='transport_price',
            field=djmoney.models.fields.MoneyField(currency_choices=[('USD', 'USD $'), ('PLN', 'PLN')], decimal_places=2, default=Decimal('0'), max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='transport_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $'), ('PLN', 'PLN')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='usd_price',
            field=djmoney.models.fields.MoneyField(currency_choices=[('PLN', 'PLN')], decimal_places=2, default=Decimal('0'), max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='usd_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_final_price',
            field=djmoney.models.fields.MoneyField(currency_choices=[('USD', 'USD $')], decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_final_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_row_price',
            field=djmoney.models.fields.MoneyField(currency_choices=[('USD', 'USD $')], decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_row_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='XYZ', editable=False, max_length=3),
        ),
    ]
