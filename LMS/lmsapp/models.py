from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField


# Create your models here.
class User(AbstractUser):    
    profile_image = models.ImageField(upload_to="Images/profile", null=True, blank=True)
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



class Course(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),        
        ('PENDING', 'PENDING'),
    )
    title = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    featured_image = models.ImageField(upload_to="Images/Featured_Image/featured_img",null=True, blank=True)
    instructor = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    featured_video = models.CharField(max_length=300,null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)
    description = RichTextField(blank=True, null=True)
    price = models.IntegerField(null=True,default=0)
    discount = models.IntegerField(null=True)

    def __str__(self):
        return self.title
    
    def course_url(self):
        from django.urls import reverse
        return reverse("coursedetails", kwargs={'slug': self.slug})

    def checkout_url(self):
        from django.urls import reverse
        return reverse("checkout", kwargs={'slug': self.slug})

    def cart_url(self):
        from django.urls import reverse
        return reverse("cart", kwargs={'slug': self.slug})

    def edit_course_url(self):
        from django.urls import reverse
        return reverse("editcourse", kwargs={'slug': self.slug})

    


class Blog(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
        ('PENDING', 'PENDING'),
    )
    title = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    featured_image = models.ImageField(upload_to="Images/Featured_Image/Blog",null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)
    description = RichTextField(blank=True, null=True)
    

    def __str__(self):
        return self.title

    def edit_blog_url(self):
        from django.urls import reverse
        return reverse("editblog", kwargs={'slug': self.slug})



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs_course = Course.objects.filter(slug=slug).order_by('-id')
    qs_blog = Blog.objects.filter(slug=slug).order_by('-id')
    exists_course = qs_course.exists()
    exists_blog = qs_blog.exists()
    if exists_course or exists_blog:
        new_slug = f"{slug}-{qs_course.first().id}" if exists_course else f"{slug}-{qs_blog.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug

@receiver(pre_save, sender=Course)
@receiver(pre_save, sender=Blog)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)