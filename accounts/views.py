from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import UserLoginForm, UserRegisterForm
from accounts.models import User


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in successfully', 'success')
                return redirect('core_app:index')
            else:
                messages.error(request, 'your email or password is not correct, try again !', 'danger')
    else:
        form = UserLoginForm()
    context = {
        'form': form,

    }
    return render(request, 'accounts/user_login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'You are logged out successfully', 'success')
    return redirect('core_app:index')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['first_name'],
                                            form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'You are registered successfully', 'success')
            return redirect('core_app:index')
        else:
            messages.success(request, 'You are not registered, try again !', 'danger')

    else:
        form = UserRegisterForm()
    context = {
        'form': form

    }
    return render(request, 'accounts/user_register.html', context)
