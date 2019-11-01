from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "accounts/index.template.html")
    
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout Successful")
    return redirect(index)
    
def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.template.html', {
            'form':form
        })
        
@login_required    
def profile(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    return render(request, 'accounts/profile.template.html', {
        'user' :user
    })
        
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have registered successful")
            else:
                messages.error(request, "You failed to register")
            return redirect(reverse('index'))
        else:
            return render(request, "accounts/register.template.html",{
                'form': form
            })
    else:
        register_form = UserRegistrationForm()
        return render(request, "accounts/register.template.html", {
            'form': register_form
        })