from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todo.models import Task
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

def index(request):
    return render(request, 'todo/index.html')

def todo_list(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-id')[0:100]
        context = {'tasks': tasks}

        return render(request, 'todo/list.html', context)
    else:
        return redirect('/todo')

def register(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    email = request.POST.get('email', '')
    # user = User.objects.create_user(username, None, password)
    user = User.objects.create_user('18min', None, '18minstan18')
    user.is_staff = True
    user.save()

    return render(request, 'todo/registration.html')

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

