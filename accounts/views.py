from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,edit_user_data
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from shop.models import shop_model
from products.models import Product


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


# profile
@login_required
def Profile (request):
    data = request.user
    products = shop_model.objects.filter(author_name = request.user)
    product_details = []
    for product in products:
        product_detail = Product.objects.get(id = product.product_id)
        product_details.append(product_detail)
    return render(request, 'profile.html', {'data':data, "products":product_details})


# edit profile
@login_required
def editProfile(request):
    if request.method == "POST":
        edit_user = edit_user_data(request.POST, instance = request.user)
        if edit_user.is_valid():
            messages.success(request, "Profile Updated")
            edit_user.save()
            return redirect("user_profile")
    else:
        edit_user = edit_user_data(instance = request.user)
    return render(request, 'edit_profile.html', {"form":edit_user})

# change password
@login_required
def changePassword (request):
    if request.method == "POST":
        pass_change_form = PasswordChangeForm(user=request.user, data = request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            update_session_auth_hash(request, pass_change_form.user)
            messages.success(request, "Password Changed")
            return redirect("user_profile")
    else:
        pass_change_form = PasswordChangeForm(user=request.user)
    return render(request, "change_password.html", {"form":pass_change_form})
