from django.contrib import admin
from .models import *

class Video_TabularInline(admin.TabularInline):
    model = Video

class course_admin(admin.ModelAdmin):
    inlines =(Video_TabularInline,)

# Register your models here.
admin.site.register(User)
admin.site.register(Course, course_admin)
admin.site.register(Categories)
admin.site.register(Blog)
admin.site.register(Lesson)
