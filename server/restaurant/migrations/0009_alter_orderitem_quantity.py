# Generated by Django 5.0.1 on 2024-02-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_remove_order_dish_order_date_order_status_orderitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]