from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout


def index(request):
    return render(request, 'account/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User not registered! Please signup first.")
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome {username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('login')
    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        # Handle signup logic here
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        allowed_domain = "srmist.edu.in"
        if not email.endswith(f"@{allowed_domain}"):
            messages.error(request, f"only{allowed_domain} emails are allowed for signup.")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, "email already exists.")
            return redirect('signup')
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully , Please login.")
        return redirect('login')
    
    return render(request, 'account/signup.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out.")
    return redirect('login')