# Generated by Django 4.2.4 on 2024-01-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0054_alter_digitalproduct_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalproduct',
            name='mobile',
            field=models.CharField(default='980000000', max_length=15, null=True),
        ),
    ]
