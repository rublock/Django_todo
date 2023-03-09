from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name='index'),
    path("signup/", views.signupuser, name="signupuser"),
    path("logout/", views.logoutuser, name="logoutuser"),
    path("login/", views.loginuser, name="loginuser"),
    path("todos/", views.todos, name="todos"),
    path("createtodos/", views.createtodos, name="createtodos"),
]