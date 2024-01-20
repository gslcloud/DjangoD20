from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
            return redirect('register')

        # Add additional input validation here (e.g., checking for unique username, strong password)

        # Perform user registration
        # ...

        messages.success(request, 'Registration successful. Please log in.')
        return redirect('user_login')

    return render(request, 'registration/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
            return redirect('user_login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('user_login')

    return render(request, 'registration/login.html')