from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['email'] == request.POST['email']:
            try:
                user = User.objects.get(email=request.POST['email'])
                return render(request,'account/signup.html',{'error':'Email already exist'})
            except User.DoesNOTExist:
                User.objects.create_user(email=request.POST['email'],password=request.POST['pass1'],name=request.POST['name'])
                user.save()
                return redirect('home')
        else:
            return render(request,'account/signup.html',{'error':'Password did not match!!'})
    else:
        return render(request,'account/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'],password=request.POST['pass1'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': 'Email or Password is Incorrect!!'})
    else:
        return render(request, 'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

