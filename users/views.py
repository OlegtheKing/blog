from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account was created successfully! Now you can log in.")
            return redirect("login")

    else:
        form = UserRegisterForm()  # django takes care of default user registration form, so you don't have to craete it manually
    # in your html, also it takes care of different types of validation
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)  # populate forms with users info
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")  # with that you don't have "you're sure you want to reload page?" browser massage
        # because it's GET request
    else:
        u_form = UserUpdateForm(instance=request.user)  # populate forms with users info
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, "users/profile.html", context)