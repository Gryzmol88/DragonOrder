# Generated by Django 4.0 on 2022-01-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_customs_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='usd_price_currency',
        ),
        migrations.AlterField(
            model_name='order',
            name='usd_price',
            field=models.FloatField(default=0),
        ),
    ]
