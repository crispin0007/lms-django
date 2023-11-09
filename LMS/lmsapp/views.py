from django.shortcuts import render, HttpResponse, render, redirect, HttpResponseRedirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render (request, 'index.html')
    

@login_required()
def dashboard(request):         
    user = request.user
    if user.is_manager:
        return render (request, 'Manager/dashboards/dashboard.html')
    elif user.is_instructor:
        return render (request, 'Instructor/dashboard.html')
    else:
        return render (request, 'Student/dashboard.html')

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
    return render (request, 'Student/settings.html')
@login_required
def wishlists(request):
    return render (request, 'Student/wishlists.html')
@login_required
def checkout(request):
    return render (request, 'Pages/checkout.html')
@login_required
def becomeinstructor(request):
    return render (request, 'Student/becomeinstructor.html')

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
    msg= None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            messages.success(request, 'User created successfully. You will be redirected to the login page shortly.')
            
            return HttpResponseRedirect('?registered=True')
        else:
            msg = "Form is not Valid"
    else:
        form = SignUpForm()
    return render(request, 'Pages/register.html', {'form': form, 'msg': msg})

