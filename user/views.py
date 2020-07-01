from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from user.forms import SignUpForm, SignInForm


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("/api/")
            else:
                return render(
                    request,
                    "user/sign_in.html",
                    {"form": form, "errors": ["Incorrect login or password"]},
                )
        else:
            return render(request, "user/sign_in.html", {"form": form})
    else:
        if request.user.is_authenticated:
            return redirect("/api/")
        else:
            form = SignInForm()
            return render(request, "user/sign_in.html", {"form": form})


def sign_up(request):
    if request.method == "POST":

        form = SignUpForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                form.cleaned_data["username"], password=form.cleaned_data["password"]
            )

            return redirect(reverse("sign_in"))
        else:
            return render(request, "user/sign_up.html", {"form": form})
    else:
        if request.user.is_authenticated:
            return redirect("/api/")
        else:
            return render(request, "user/sign_up.html", {"form": SignUpForm()})


@login_required(login_url=reverse_lazy("sign_in"))
def logout_view(request):
    logout(request)
    return redirect(reverse("sign_in"))
