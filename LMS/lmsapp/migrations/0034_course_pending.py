# Generated by Django 4.2.4 on 2024-01-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0033_alter_blog_description_alter_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='pending',
            field=models.BooleanField(default=True),
        ),
    ]
