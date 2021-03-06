# Generated by Django 4.0 on 2021-12-30 20:45

from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_order', models.DateField()),
                ('status', models.CharField(choices=[('W przygotowaniu', 'W przygotowaniu'), ('Zamówiono', 'Zamówiono'), ('Wysłano', 'Wysłano'), ('Dostarczono', 'Dostarczono')], default='W przygotowaniu', max_length=15)),
                ('product_price_currency', djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN'), ('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('product_price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=8)),
                ('transport_price_currency', djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN'), ('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('transport_price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=8)),
                ('total_weight', models.FloatField()),
                ('all_items', models.IntegerField()),
                ('total_transport_price_currency', djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN'), ('USD', 'USD $')], default='PLN', editable=False, max_length=3)),
                ('total_transport_price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='PLN', max_digits=8)),
                ('customs_price_currency', djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN'), ('USD', 'USD $')], default='PLN', editable=False, max_length=3)),
                ('customs_price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='PLN', max_digits=8)),
                ('fee_per_kg_currency', djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN'), ('USD', 'USD $')], default='PLN', editable=False, max_length=3)),
                ('fee_per_kg', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='PLN', max_digits=8)),
                ('total_price_currency', djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN'), ('USD', 'USD $')], default='PLN', editable=False, max_length=3)),
                ('total_price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='PLN', max_digits=8)),
            ],
            options={
                'ordering': ('-date_of_order',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('purchase_row_price_currency', djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN'), ('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('purchase_row_price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=8)),
                ('quantity', models.IntegerField()),
                ('purchase_final_price_currency', djmoney.models.fields.CurrencyField(choices=[('PLN', 'PLN'), ('USD', 'USD $')], default='PLN', editable=False, max_length=3)),
                ('purchase_final_price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='PLN', max_digits=8)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
