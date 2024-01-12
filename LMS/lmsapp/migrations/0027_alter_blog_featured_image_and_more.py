# Generated by Django 4.2.4 on 2024-01-10 06:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0026_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='Images/Featured_Image/Blog'),
        ),
        migrations.AlterField(
            model_name='course',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='Images/Featured_Image/featured_img'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='Images/profile'),
        ),
    ]