# Generated by Django 4.2.4 on 2024-01-12 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0039_rename_name_categories_title_remove_user_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='slug',
        ),
    ]
