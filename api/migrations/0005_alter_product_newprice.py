# Generated by Django 5.1.6 on 2025-02-09 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_newprice_yes_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='newPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Новаціна по Акцій'),
        ),
    ]
