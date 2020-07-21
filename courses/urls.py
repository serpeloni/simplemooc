from django.urls import path
from .views import announcements, enrollment, index, details, undo_enrollment

urlpatterns = [
    path("", index, name="index"),
    # path("<int:pk>/", details, name="details"),
    path("<str:slug>/", details, name="details"),
    path("<str:slug>/inscricao/", enrollment, name="enrollment"),
    path("<str:slug>/cancelar-inscricao/", undo_enrollment, name="undo_enrollment"),
    path("<str:slug>/anuncios/", announcements, name="announcements"),
]
