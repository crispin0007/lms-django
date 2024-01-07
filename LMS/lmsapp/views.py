from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from lmsapp.models import Categories
from lmsapp.models import User
# Create your views here.

def home(request):
    category = Categories.objects.all()
    context ={
        'category':category
    }
    return render (request, 'index.html', context)
    

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
def mylearning(request):
    return render (request, 'Student/mylearning.html')
@login_required
def messages(request):
    return render (request, 'Student/messages.html')
@login_required
def mycart(request):
    return render (request, 'Student/mycart.html')
@login_required
def settings(request):
    return render (request, 'required_login_pages/settings.html')
@login_required
def wishlists(request):
    return render (request, 'Student/wishlists.html')
@login_required
def checkout(request):
    return render (request, 'Pages/checkout.html')
@login_required
def becomeinstructor(request):
    return render (request, 'Student/becomeinstructor.html')

def coursedetails(request):
    return render(request, ('Pages/course_detail.html'))

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
            user = form.save()
            return HttpResponseRedirect('?registered=True')
        else:
           print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'Pages/register.html', {'form': form, 'success_msg': success_msg})

def update_profile(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        user_bio = request.POST.get('user_bio')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.user_bio = user_bio
        user.save()
        return HttpResponseRedirect('?update=True')
        success_msg = "User Updated successfully"
        # return redirect('settings')








