# Generated by Django 4.2.4 on 2024-01-08 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0020_alter_user_email_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_token',
            field=models.CharField(default='', max_length=200),
        ),
    ]
