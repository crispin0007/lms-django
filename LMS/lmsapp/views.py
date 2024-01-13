from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, get_object_or_404
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from lmsapp.models import Categories, Course, User, Blog, Lesson, Video
from lmsapp.utils import send_email_token
from django.core.mail import send_mail
from django.conf import settings
import uuid
from django.urls import reverse
from django.http import JsonResponse
import requests
import json
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    category = Categories.objects.all()
    course = Course.objects.all()
    context ={
        'category':category,
        'course':course
    }
    return render (request, 'index.html', context)
    
def course_details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    lesson = Lesson.objects.filter(course=course)
    video = Video.objects.filter(course=course)
    context = {
        'course': course,
        'lesson' : lesson,
        'video':video,
    }
    return render (request, 'Pages/course_detail.html', context)

@login_required
def account_details(request, slug):
    acc_detail = get_object_or_404(User, slug=slug)

    context = {
        'acc_detail': acc_detail
    }
    return render (request, 'Manager/user_profile.html', context)

@login_required()
def dashboard(request):         
    user = request.user
    if user.is_manager:
        return render (request, 'Manager/dashboard.html')
    elif user.is_instructor:
        return render (request, 'Instructor/dashboard.html')
    else:
        return render (request, 'Student/dashboard.html')

@login_required
def profile(request):
    user = request.user
    return render (request, 'required_login_pages/profile.html')

@login_required
def mycourses(request):
    course = Course.objects.all()

    context = {
        'course' : course
    }
    return render (request, 'Student/mycourses.html',context)

@login_required
def myblogs(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog,
    }
    return render(request, 'Student/myblogs.html', context)

@login_required
def messages(request):
    return render (request, 'Student/messages.html')

@login_required
def notifications(request):
    return render (request, 'Student/notifications.html')

@login_required
def cart(request, slug):
    course = Course.objects.all()
    try:
        course = Course.objects.get(slug=slug)
    except Course.DoesNotExist:
        return redirect('index.html')

    context = {
        'course' : course
    }
    return render (request, 'Student/mycart.html', context)

@login_required
def settings(request):
    return render (request, 'required_login_pages/settings.html')

@login_required
def wishlists(request):
    return render (request, 'Student/wishlists.html')

@login_required
def checkout(request, slug):
    user = request.user
    course = Course.objects.all()
    try:
        course = Course.objects.get(slug=slug)
    except Course.DoesNotExist:
        return redirect('index.html')

    context = {
        'course' : course
    }
    return render (request, 'Pages/checkout.html',context)


@login_required
def edit_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    category = Categories.objects.all()

    context = {
        'course': course,
        'category': category
    }
    return render(request, 'required_login_pages/edit_course.html', context)

@login_required
def edit_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    category = Categories.objects.all()

    context = {
        'blog': blog,
        'category': category
    }
    return render(request, 'required_login_pages/edit_blog.html', context)

@login_required
def addblog(request):
    category = Categories.objects.all()
    context = {
        'category': category
    }
    return render(request, 'required_login_pages/addblog.html',context)

@login_required
def addcourse(request):
    category = Categories.objects.all()
    context = {
        'category': category
    }
    return render(request, 'required_login_pages/addcourse.html',context)



@login_required
def becomeinstructor(request):
    return render (request, 'Student/becomeinstructor.html')

@login_required
def purchasehistory(request):
    return render(request, 'Student/purchasehistory.html')

@login_required
def myfeedbacks(request):
     return render(request, 'Student/myfeedbacks.html')

def blog(request):
    return render(request, ('Pages/blog.html'))

def error_404(request, exception):
    render(request, ('Pages/404.html'))
    
def error_500(request):
    render(request, ('Pages/500.html'))

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            remember_me = request.POST.get('remember_me')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request, user)
                return redirect('dashboard')
            else:
                msg = 'Invalid Credentials'
        else:
            msg = 'Error Validatng Form'
    
    return render(request,'Pages/login.html', {'form': form, 'msg': msg})

def register(request):
    success_msg = "User created successfully. You will be redirected to the login page shortly."
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            user = form.save()
            email_token = str(user.email_token)
            send_email_token(email, email_token)
            
            return HttpResponseRedirect('?registered=True')
        else:
           print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'Pages/register.html', {'form': form, 'success_msg': success_msg})

def verify(request, token):
    try:
        profile = User.objects.get(email_token=token)
        if not profile.is_verified:
            profile.is_verified = True
            profile.is_student = True
            profile.save()
            login(request, profile)
            return render(request, 'index.html')
        else:
            return render(request, 'index.html')
    except User.DoesNotExist:
        return HttpResponse('not working')


# ==================update==================
@login_required
def update_profile(request):
    success_msg = "User Updated successfully"
    if request.method == "POST":
        user_id = request.user.id
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        user_bio = request.POST.get('user_bio')
        
        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.user_bio = user_bio
        user.save()
        return HttpResponseRedirect('?update=True')
        
    return render (request, 'required_login_pages/settings.html')


@login_required
def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        category_name = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        featured_image = request.FILES.get('featured_image')

        category_instance = Categories.objects.get(name=category_name)

        course.title = title
        course.category = category_instance
        course.description = description
        course.price = price
        course.discount = discount

        if featured_image:
            course.featured_image = featured_image

        course.save()

        return redirect('list_course')
    else:
        return HttpResponseBadRequest("Invalid request method")

    return render(request, 'Manager/dashboard.html', {'course': course})

@login_required
def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        category_name = request.POST.get('category')
        description = request.POST.get('description')
        featured_image = request.FILES.get('featured_image')

        category_instance = Categories.objects.get(name=category_name)

        blog.title = title
        blog.category = category_instance
        blog.description = description


        if featured_image:
            blog.featured_image = featured_image

        blog.save()

        return redirect('myblogs')
    else:
        return HttpResponseBadRequest("Invalid request method")

    return render(request, 'Manager/dashboard.html', {'blog': blog})



# ============Approval==============
@login_required
def approval_course (request):
    course = Course.objects.all()
    context = {
        'course' : course
    }
    return render(request, 'Manager/Approval/course.html',context)
@login_required
def approval_blog (request):
    blog = Blog.objects.all()
    context = {
        'blog' : blog
    }
    return render(request, 'Manager/Approval/blog.html', context)

@login_required
def approval_instructor (request):
    ins_list = User.objects.all()
    context = {
        'ins_list' : ins_list
    }
    return render(request, 'Manager/Approval/instructor.html',context)

# ===============delete===============
@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.delete()
        return redirect('list_course')

    return render(request, 'Manager/Approval/course.html', {'course': course})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        blog.delete()
        return redirect('list_blog')

    return render(request, 'Manager/Approval/blog.html', {'blog': blog})

# ===============publish ==================
# ============lists==============
@login_required
def publish_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.status = 'PUBLISH'
        course.save()
        return redirect('list_course')

    return render(request, 'Manager/Approval/course.html', {'course': course})

@login_required
def publish_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        blog.status = 'PUBLISH'
        blog.save()
        return redirect('list_blog')

    return render(request, 'Manager/Approval/blog.html', {'blog': blog})

@login_required
def approve_instructor(request, user_id):
    instructor = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        instructor.status = 'INSTRUCTOR'
        instructor.is_instructor = True
        instructor.is_student = False
        instructor.save()
        return redirect('list_instructor')

    return render(request, 'Manager/Approval/instructor.html', {'instructor': instructor})
# ===============unpublish==================
@login_required
def unpublish_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.status = 'PENDING'
        course.save()
        return redirect('list_course')

    return render(request, 'Manager/Approval/course.html', {'course': course})

@login_required
def unpublish_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        blog.status = 'PENDING'
        blog.save()
        return redirect('list_blog')

    return render(request, 'Manager/Approval/blog.html', {'blog': blog})

@login_required
def unapprove_instructor(request, user_id):
    instructor = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        instructor.status = 'STUDENT'
        instructor.is_instructor = False
        instructor.is_student = True
        instructor.save()
        return redirect('list_instructor')

    return render(request, 'Manager/Approval/instructor.html', {'instructor': instructor})

@login_required
def request_instructor(request, user_id):
    student = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        student.status = 'STUDENT'
        student.is_student = True
        student.status = 'PENDING'
        student.save()  
        return redirect('becomeinstructor')

    return render(request, 'Student/dashboard.html', {'student': student})

@login_required
def create_course(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        featured_image = request.FILES.get('featured_image')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        status = request.POST.get('status', 'DRAFT')

        if status == 'PUBLISH':
            status = 'PENDING'

        new_course = Course.objects.create(
            title=title,
            instructor=request.user,
            category=Categories.objects.get(id=category_id),
            description=description,
            price=price,
            discount=discount,
            featured_image=featured_image,
            status=status   
        )

        return redirect('add_lesson', course_id=new_course.id)

    categories = Categories.objects.all()

    return render(request, 'Student/courses.html', {'categories': categories})

@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        featured_image = request.FILES.get('featured_image')
        status = request.POST.get('status', 'DRAFT')

        if status == 'PUBLISH':
            status = 'PENDING'

        new_blog = Blog.objects.create(
            title=title,
            user=request.user,
            category=Categories.objects.get(id=category_id),
            description=description,
            featured_image=featured_image,
            status=status   
        )

        return redirect('myblogs')

    categories = Categories.objects.all()

    return render(request, 'Student/myblogs.html', {'categories': categories})

@login_required
def blog_status_function(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        new_status = request.POST.get('new_status')

        if new_status in ['DRAFT', 'PUBLISH', 'PENDING']:
            if new_status == 'PUBLISH':
                new_status = 'PENDING'
            blog.status = new_status
            blog.save()
        elif new_status == 'DELETE':
            blog.delete()
            return redirect('myblogs') 
    return redirect('myblogs')

@login_required
def course_status_function(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        new_status = request.POST.get('new_status')

        if new_status in ['DRAFT', 'PUBLISH', 'PENDING']:
            if new_status == 'PUBLISH':
                new_status = 'PENDING'
            course.status = new_status
            course.save()
        elif new_status == 'DELETE':
            course.delete()
            return redirect('mycourses') 
    return redirect('mycourses')

# ================list============

@login_required
def list_course (request):
    course = Course.objects.all()
    context = {
        'course' : course
    }
    return render(request, 'Manager/List/course.html',context)


@login_required
def list_blog (request):
    blog = Blog.objects.all()
    context = {
        'blog' : blog
    }
    return render(request, 'Manager/List/blog.html', context)


@login_required
def list_instructor (request):
    ins_list = User.objects.all()
    context = {
        'ins_list' : ins_list
    }
    return render(request, 'Manager/List/instructor.html', context)


@login_required
def list_student (request):
    std_list = User.objects.all()
    context = {
        'std_list' : std_list
    }
    return render(request, 'Manager/List/student.html',context)

# ================income================

@login_required
def total_income(request):
    return render(request, 'Manager/income.html')


@login_required
def all_feedbacks(request):
    return render(request, 'Manager/feedback.html')


@login_required
def top_course(request):
    return render(request, 'Manager/top_course.html')



# lessons veiws

@login_required
def add_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lesson_set.all() 
    return render(request, 'required_login_pages/add_lesson.html', {'course': course, 'lessons': lessons})


@login_required
def add_lesson_name(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        new_lesson = Lesson.objects.create(
            name=title,
            course=course
        )
        redirect_url = reverse('add_lesson', kwargs={'course_id': course.id})

        return redirect(redirect_url)

    return render(request, 'Student/mycourses.html')


@login_required
def add_chapter(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == 'POST':  
        course_id = request.POST.get('course_id')  
        course_title = lesson.course  
        serial_number = request.POST.get('serial')
        title = request.POST.get('title')
        video_url = request.POST.get('url')
        thumbnail = request.FILES.get('Thumbnail')
        preview = request.POST.get('exampleCheck1', False)
        
        try:
            time_duration = float(request.POST.get('time_duration', 0.0))
        except ValueError:
            time_duration = 0.0

        video = Video(
            serial_number=serial_number,
            title=title,
            video_url=video_url,
            thumbnail=thumbnail,
            preview=preview,
            time_duration=2 ,
            lesson=lesson,
            course=course_title,
            course_id=course_id            
        )
        try:
            video.full_clean() 
            video.save()
            return redirect('add_lesson', course_id=course_id) 
        except ValidationError as e:
            error_message = ', '.join(e.messages)
            return redirect('add_lesson', course_id=course_id)

    return render(request, 'Student/mycourses.html', {'lesson': lesson})



def test(request):
    return render(request, 'Student/learning_area.html')

@csrf_exempt
@login_required
def khalti_response(request):
    if request.method == 'POST':
        # Parse the JSON data from the request body
        data = json.loads(request.body)

        # Extract relevant information from the Khalti payload
        user = request.user
        product_name = data.get('product_name')
        transaction_id = data.get('idx')
        amount = data.get('amount')
        mobile = data.get('mobile')

        # Save the payment information to the database
        digital_product = DigitalProduct.objects.create(
            user=user,
            product_name=product_name,
            transaction_id=transaction_id,
            amount=amount,
            mobile=mobile,
            # Add other fields as needed
        )
        digital_product.save()

        # Return a success response
        return JsonResponse({'status': 'success'})

    # If the request method is not POST, return an error response
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})