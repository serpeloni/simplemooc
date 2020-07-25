from django.urls import path
from .views import (
    announcements,
    enrollment,
    index,
    details,
    lesson,
    lessons,
    material,
    show_announcement,
    undo_enrollment,
)

urlpatterns = [
    path("", index, name="index"),
    # path("<int:pk>/", details, name="details"),
    path("<str:slug>/", details, name="details"),
    path("<str:slug>/inscricao/", enrollment, name="enrollment"),
    path("<str:slug>/cancelar-inscricao/", undo_enrollment, name="undo_enrollment"),
    path("<str:slug>/anuncios/", announcements, name="announcements"),
    path("<str:slug>/anuncios/<int:pk>", show_announcement, name="show_announcement"),
    path("<str:slug>/aulas/", lessons, name="lessons"),
    path("<str:slug>/aulas/<int:pk>", lesson, name="lesson"),
    path("<str:slug>/materiais/<int:pk>", material, name="material"),
]
