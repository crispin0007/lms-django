# Generated by Django 4.2.4 on 2024-01-12 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0041_categories_slug_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='not_is_verified_instructor',
            field=models.BooleanField(default=True),
        ),
    ]
