# Generated by Django 4.2.4 on 2024-01-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0053_alter_digitalproduct_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalproduct',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
