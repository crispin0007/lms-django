from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField


# Create your models here.
class User(AbstractUser): 
    STATUS = (
        ('STUDENT','STUDNET'),        
        ('PENDING', 'PENDING'),
        ('INSTRUCTOR', 'INSTRUCTOR'),
    )   
    profile_image = models.ImageField(upload_to="Images/profile", null=True, blank=True, default='img/team-1.jpg')
    is_manager = models.BooleanField('Is manager', default=False)
    is_instructor = models.BooleanField('Is instructor', default=False)
    is_student = models.BooleanField('Is student', default=True)
    user_bio = models.TextField(default='', max_length=200, null=True, blank=True)
    email_token = models.UUIDField(default=uuid.uuid4, editable=False)
    is_verified = models.BooleanField(default=False)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True, default="STUDENT")

    def account_detail_url(self):
        from django.urls import reverse
        return reverse("accdetails", kwargs={'slug': self.slug})

class Categories (models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
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

    def learning_area_url(self): 
        from django.urls import reverse
        return reverse("learning_area", kwargs={'slug': self.slug})

    def add_lesson_url(self): 
        from django.urls import reverse
        return reverse("add_lesson", kwargs={'slug': self.slug})

    


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
    
    def blog_url(self):
        from django.urls import reverse
        return reverse("blogdetails", kwargs={'slug': self.slug})



# ==================================slug creator=======================
def create_slug(instance, new_slug=None):
    if isinstance(instance, (Course, Blog)):
        source_field = 'title'
    elif isinstance(instance, User):
        source_field = 'username'
    elif isinstance(instance, Categories):
        source_field = 'name'
    else:
        raise ValueError("Unsupported model type for slug generation")

    
    slug = slugify(getattr(instance, source_field))

    if new_slug is not None:
        slug = new_slug

    model_class = instance.__class__
    qs = model_class.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()

    if exists:
        new_slug = f"{slug}-{qs.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug

@receiver(pre_save, sender=Course)
@receiver(pre_save, sender=Blog)
@receiver(pre_save, sender=Categories)
@receiver(pre_save, sender=User)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__ (self):
        return self.name + " - " + self.course.title 

class Video(models.Model):
    serial_number = models.IntegerField(null=True)
    thumbnail = models.ImageField(upload_to="Images/Lesson", null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    video_url = models.CharField(max_length= 200)
    time_duration = models.FloatField(null=True)
    preview = models.BooleanField(default=False) 

    def __str__(self):
        return self.title


class DigitalProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    product_identity = models.IntegerField(null=True,default=0)
    product_name = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=255, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    mobile = models.CharField(max_length=15, default="980000000", null=True)  

    def __str__(self):
        return f'{self.user.username} - {self.product_name} - Transaction ID: {self.transaction_id}'

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.sender.username} to {self.receiver.username} - {self.timestamp}"


# Recommendations
class SearchQuery(models.Model):
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query




