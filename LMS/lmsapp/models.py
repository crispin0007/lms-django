from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_manager = models.BooleanField('Is manager', default=False)
    is_instructor = models.BooleanField('Is instructor', default=False)
    is_student = models.BooleanField('Is student', default=True)

class Course(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    # instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    enrollment_limit = models.PositiveIntegerField()
    prerequisites = models.TextField()
    skills_taught = models.TextField()
    course_duration = models.PositiveIntegerField()
    lectures = models.PositiveIntegerField()
    total_students_enrolled = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    thumbnail = models.ImageField(upload_to='course_thumbnails/')
    syllabus = models.TextField()
    requirements = models.TextField()
    target_audience = models.TextField()
    publish_date = models.DateField()
    last_updated_date = models.DateField()
    video_url = models.URLField()
    # course_materials = models.ManyToManyField('CourseMaterial', blank=True)
    promotional_video = models.URLField()
    certificate = models.ImageField(upload_to='course_certificates/', blank=True, null=True)

    def __str__(self):
        return self.title