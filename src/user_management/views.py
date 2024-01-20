from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse

def register_user(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))  # Use reverse to dynamically generate the URL
        else:
            # Add error handling for invalid form data
            return render(request, 'register.html', {'form': form, 'error': 'Invalid form data'})
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})