# Generated by Django 4.2.4 on 2024-01-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0031_alter_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('PUBLISH', 'PUBLISH'), ('DRAFT', 'DRAFT'), ('PENDING', 'PENDING')], max_length=100, null=True),
        ),
    ]
