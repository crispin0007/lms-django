# Generated by Django 4.2.4 on 2024-01-12 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0038_categories_slug_user_slug_alter_user_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]