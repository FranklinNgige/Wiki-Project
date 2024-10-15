from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()
            # Log the user in directly without needing to re-authenticate
            login(request, user)
            messages.success(request, 'Account created and logged in successfully!')
            return redirect('home')
        else:
            # If form is invalid, add an error message
            messages.error(request, 'There was an error creating your account. Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


def reset_password(request):
    # Handle password reset logic here
    if request.method == 'POST':
        # Assume we will look for email and implement reset logic here
        email = request.POST.get('email')
        # Add logic to send a reset email
        messages.success(request, 'Password reset instructions have been sent to your email.')
    return render(request, 'reset_password.html')
