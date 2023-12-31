# Generated by Django 4.2.4 on 2024-01-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0004_categories_remove_course_certificate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('author_image', models.ImageField(upload_to='Images/Authors')),
                ('author_bio', models.TextField()),
            ],
        ),
    ]
