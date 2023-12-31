# Generated by Django 4.2.4 on 2024-01-07 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0009_remove_instructor_is_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Images/profile'),
            preserve_default=False,
        ),
    ]
