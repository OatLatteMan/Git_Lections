from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todo.models import Task, Register
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'desc': forms.Textarea(attrs={'class': 'textarea'}),
        }

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['login', 'password', 'email']
        widgets = {
            'login': forms.TextInput(attrs={'class': 'login'}),
            'password': forms.Textarea(attrs={'class': 'password'}),
            'email': forms.Textarea(attrs={'class': 'email'}),
        }

def index(request):
    return render(request, 'todo/index.html')

def todo_list(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-id')[0:100]
        context = {'tasks': tasks}

        return render(request, 'todo/list.html', context)
    else:
        return redirect('/todo')

def todo_detail(request, number):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=number)
        context = {'task': task,}
        if task.user == request.user:
            return render(request, 'todo/detail.html', context)
    else:
        return redirect('/todo')

def todo_new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            print(task, task.id)
            return redirect('/todo/list')
        else:
            form = TaskForm(request.POST)
            return render(request, 'todo/new.html', {'form': form})
    else:
        form = TaskForm()
        return render(request, 'todo/new.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            reg = form.save()
            print(reg)
            return redirect('/todo/list')
        else:
            form = RegisterForm(request.POST)
            return render(request, 'todo/registration.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'todo/registration.html', {'form': form})

# def register(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     print(request.POST, "<<<<<<<<<<<<<")
#     # email = request.POST.get('email97', '')
#     user = User.objects.create_user(username=username, password=password)
#     # user = User.objects.create_user('18min', None, '1234')
#     user.is_staff = True
#     user.save()

#     return render(request, 'todo/registration.html')

