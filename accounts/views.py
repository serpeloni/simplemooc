from re import template
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset
from core.utils import generate_hash_key
from courses.models import Enrollment

User = get_user_model()

# Create your views here.
@login_required
def dashboard(request):
    template_name = "accounts/dashboard.html"
    context = {}
    return render(request, template_name, context)


def register(request):
    template_name = "accounts/register.html"
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data["password1"]
            )
            login(request, user)
            return redirect("core:home")
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, template_name, context)


def password_reset(request):
    template_name = "accounts/password_reset.html"
    form = PasswordResetForm(request.POST or None)
    context = {}
    if form.is_valid():
        form.save()
        context["success"] = True
    context["form"] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = "accounts/password_request_confirm.html"
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    context = {}
    if form.is_valid():
        form.save()
        context["success"] = True

    context["form"] = form
    return render(request, template_name, context)


@login_required
def edit(request):
    template_name = "accounts/edit.html"
    context = {}
    if request.method == "POST":
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Os dados da sua conta foram alterados com sucesso"
            )
            return redirect("accounts:dashboard")
    else:
        form = EditAccountForm(instance=request.user)
    context["form"] = form
    return render(request, template_name, context)


@login_required
def edit_password(request):
    template_name = "accounts/edit_password.html"
    context = {}
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context["success"] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context["form"] = form
    return render(request, template_name, context)
