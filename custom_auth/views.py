from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm


# from .models import UserProfile


def register(request):
    if request.user.is_authenticated:
        return redirect('team_list')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)  # Save the user using the custom user model
            login(request, user)  # Log the user in
            return redirect('team_list')  # Redirect to the team_list view
    else:
        form = RegisterForm()
    return render(request, 'custom_auth/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('team_list')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('team_list')  # Redirect to a success page
        else:
            return render(request, 'custom_auth/login.html', {'error': 'Invalid username or password'})
    return render(request, 'custom_auth/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout