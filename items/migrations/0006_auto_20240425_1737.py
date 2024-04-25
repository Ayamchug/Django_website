# Generated by Django 3.1.2 on 2024-04-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_remove_item_non_availablity_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('SZ', 'Sizzlers'), ('PS', 'Pasta'), ('AP', 'Appetizers'), ('PZ', 'Pizzas'), ('DS', 'Desserts'), ('CM', 'Combos')], max_length=50),
        ),
    ]
