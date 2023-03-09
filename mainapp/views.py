from django.views.generic import TemplateView
from mainapp import models
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["objects"] = models.DataBase.objects.all()
        return context
    
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'mainapp/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/todos/')
            except IntegrityError:
                return render(request, 'mainapp/signupuser.html', {'form': UserCreationForm(), 'error':'This username is already in use'})
        else:
            # Tell the user that password didn't match
            return render(request, 'mainapp/signupuser.html', {'form': UserCreationForm(), 'error':'Password did not match'})
        
def todos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'mainapp/todos.html', {'todos': todos })

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'mainapp/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'mainapp/loginuser.html', {'form': AuthenticationForm(), 'error': 'User name and password did not match'})
        else:
            login(request, user)
            return redirect('/todos/')

def createtodos(request):
    if request.method == 'GET':
        return render(request, 'mainapp/createtodos.html', {'todoform': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('/')
        except ValueError:
            return render(request, 'mainapp/createtodos.html', {'error': 'Field text is too long'})
