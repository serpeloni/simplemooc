from django.urls import path
from .views import index, reply_correct, reply_incorrect, thread

urlpatterns = [
    path("", index, name="index"),
    path("tag/<str:tag>", index, name="index_tagged"),
    path("<str:slug>", thread, name="thread"),
    path("respostas/<int:pk>/correta", reply_correct, name="reply_correct"),
    path("respostas/<int:pk>/incorreta", reply_incorrect, name="reply_incorrect"),
]

