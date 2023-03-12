from django.views.generic import TemplateView
from mainapp import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import UserTodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from mainapp.forms import UserLoginForm, UserTodoForm


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"
    
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

@login_required        
def todos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'mainapp/todos.html', {'todos': todos })

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'mainapp/loginuser.html', {'form': UserLoginForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'mainapp/loginuser.html', {'form': UserLoginForm(), 'error': 'User name and password did not match'})
        else:
            login(request, user)
            return redirect('/todos/')

@login_required
def createtodos(request):
    if request.method == 'GET':
        return render(request, 'mainapp/createtodos.html', {'todoform': UserTodoForm()})
    else:
        try:
            form = UserTodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('/')
        except ValueError:
            return render(request, 'mainapp/createtodos.html', {'error': 'Data error'})

@login_required
def todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        formtodo = UserTodoForm(instance=todo)
        return render(request, 'mainapp/todo.html', {'todo': todo, 'formtodo': formtodo })
    else:
        try:
            formtodo = UserTodoForm(request.POST, instance=todo)
            formtodo.save()
            return redirect('/todos/')
        except ValueError:
            return render(request, 'mainapp/todo.html', {'todo': todo, 'formtodo': formtodo, 'error': 'Data error' })

@login_required        
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('/todos/')

@login_required    
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('/todos/')

@login_required    
def completedtodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'mainapp/completedtodos.html', {'todos': todos })
