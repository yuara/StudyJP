from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.IndexVoca.as_view(), name="index"),
    path("all", views.ListVoca.as_view(), name="all"),
    path("quiz/<level>", views.QuizVoca.as_view(), name="quiz"),
]
