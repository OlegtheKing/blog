from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()  # django takes care of default user registration form, so you don't have to craete it manually
    # in your html, also it takes care of different types of validation
    return render(request, "users/register.html", {"form": form})
