# Generated by Django 4.2 on 2023-05-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_produit_promotions_produit_promotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]
