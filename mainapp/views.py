from django.views.generic import TemplateView
from mainapp import models
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login


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
    return render(request, 'mainapp/todos.html')