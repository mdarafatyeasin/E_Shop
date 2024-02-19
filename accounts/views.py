from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# registration
def UserRegistration(request):
    if request.method == "POST":
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            messages.success(request, 'User created successfully!!!')
            reg_form.save(commit=True)
            print(reg_form)
            return redirect('home')
    else:
        reg_form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': reg_form})

# login
def UserLogin (request):
    if request.method == "POST":
        login_form = AuthenticationForm(request = request, data = request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.success(request, "Welcome Back!")
                login(request, user)
                return redirect('home')
            else:
                return redirect('user_registration')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'form':login_form})

# logout
@login_required
def Logout(request):
   logout(request) 
   messages.warning(request, "Please login again")
   return redirect('home')
