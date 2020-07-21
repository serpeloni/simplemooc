from django.urls import path
from django.contrib.auth import views
from .views import (
    password_reset,
    password_reset_confirm,
    register,
    dashboard,
    edit,
    edit_password,
)

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path(
        "entrar/",
        views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("sair/", views.LogoutView.as_view(next_page="core:home"), name="logout"),
    path("cadastre-se/", register, name="register"),
    path("nova-senha/", password_reset, name="password_reset"),
    path(
        "confirmar-nova-senha/<str:key>/",
        password_reset_confirm,
        name="password_reset_confirm",
    ),
    path("editar/", edit, name="edit"),
    path("editar-senha/", edit_password, name="edit_password"),
]
