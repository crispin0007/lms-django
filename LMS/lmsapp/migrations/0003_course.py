# Generated by Django 4.2.4 on 2023-11-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0002_alter_user_is_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('subcategory', models.CharField(blank=True, max_length=50, null=True)),
                ('level', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('enrollment_limit', models.PositiveIntegerField()),
                ('prerequisites', models.TextField()),
                ('skills_taught', models.TextField()),
                ('course_duration', models.PositiveIntegerField()),
                ('lectures', models.PositiveIntegerField()),
                ('total_students_enrolled', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('thumbnail', models.ImageField(upload_to='course_thumbnails/')),
                ('syllabus', models.TextField()),
                ('requirements', models.TextField()),
                ('target_audience', models.TextField()),
                ('publish_date', models.DateField()),
                ('last_updated_date', models.DateField()),
                ('video_url', models.URLField()),
                ('promotional_video', models.URLField()),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='course_certificates/')),
            ],
        ),
    ]
