from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['email'] == request.POST['email']:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken!!')
                return redirect('vsup')
            else:
                user = User.objects.create_User(name=name, email=email, password=password)
                user.save()
                messages.success(request, 'You are Registered!')
        else:
            messages.error(request, 'Password did not match')
            return redirect('vsup')
    else:
        return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in!!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Email OR Password!!')
            return redirect('vlog')
    else:
        return render(request, 'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

