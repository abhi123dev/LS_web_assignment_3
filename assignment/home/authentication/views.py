from django.shortcuts import render,redirect
from .models import*
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url = "/login/")

def index(request):
    return render(request , "home/index.html")

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request , 'Invalid Username' )
            return redirect('/login/')
    
        user = authenticate(username = username ,password= password)

        if user is None:
            messages.error(request , 'Invalid Password' )
            return redirect('/login/')
    
        else:
            login(request , user)
            return redirect('/index/')



    return render(request , 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        my_email = request.POST.get('my_email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            
        )

        user.set_password(password)
        user.save()

        messages.info(request , 'Account created successfuly' )

        return redirect('/register/')

    return render(request , 'register.html')