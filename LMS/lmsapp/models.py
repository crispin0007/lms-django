from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class User(AbstractUser):    
    profile_image = models.ImageField(upload_to="Images/profile", null=True, blank=True, default='')
    is_manager = models.BooleanField('Is manager', default=False)
    is_instructor = models.BooleanField('Is instructor', default=False)
    is_student = models.BooleanField('Is student', default=True)
    user_bio = models.TextField(default='', max_length=200, null=True, blank=True)
    email_token = models.UUIDField(default=uuid.uuid4, editable=False)
    is_verified = models.BooleanField(default=False)

class Categories (models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=100, null=True)
    instructor_cover = models.ImageField(upload_to="Images/Instructors")
    instructor_bio = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )
    title = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    featured_image = models.ImageField(upload_to="Images/Featured_Image/featured_img",null=True)
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    featured_video = models.CharField(max_length=300,null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)
    description = models.TextField()
    price = models.IntegerField(null=True,default=0)
    discount = models.IntegerField(null=True)

    def __str__(self):
        return self.title

  