from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

def projecthomepage(request):
    return render(request, 'projectapp/ProjectHomePage.html')

def registerpagecall(request):
    return render(request, 'projectapp/register.html')  # Ensure the path is correct

def loginpagecall(request):
    return render(request, 'projectapp/login.html')  # Ensure the path is correct

def registerpagelogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Using get() for safety
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')  # Matches your HTML field
        password2 = request.POST.get('password2')  # Matches your HTML field

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('registerpagecall')

        try:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, "Registration successful.")
            return redirect('loginpagelogic')  # Redirect to login after registration
        except Exception as e:
            messages.error(request, str(e))
            return redirect('registerpagecall')

    return render(request, 'projectapp/register.html')


@csrf_exempt
def loginpagelogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if username == 'admin':
                return redirect('adminapp:adminhomepage')
            else:
                return redirect('userapp:userhomepage')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('loginpagecall')

    return render(request, 'projectapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')


def aboutus(request):
    return render(request, 'projectapp/AboutUs.html')


def elibrary(request):
    return render(request, 'projectapp/E-library.html')


def authentication(request):
    return render(request, 'projectapp/Authentication.html')


def digital(request):
    return render(request, 'projectapp/Digital.html')
