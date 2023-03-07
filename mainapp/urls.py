from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view()),
    path("signup/", views.signupuser, name="signupuser"),
    path("todos/", views.todos, name="todos"),
]