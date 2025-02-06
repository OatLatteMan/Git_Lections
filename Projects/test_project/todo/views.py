from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import Task
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'desc']

def index(request):
    return render(request, 'todo/index.html')

def todo_list(request):
    tasks = Task.objects.all().order_by('-id')[0:100]

    context = {
        'tasks': tasks
    }

    return render(request, 'todo/list.html', context)

def todo_new(request):
    form = TaskForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            print(task, task.id)
            return redirect('/todo/list')
        else:
            form = TaskForm(request.POST)
            return render(request, 'todo/new.html', context)
    else:
        form = TaskForm()
        return render(request, 'todo/new.html', context)


def todo_detail(request, number):
    task = Task.objects.get(id=number)

    context = {
        'task': task,
        'number': number,
    }

    return render(request, 'todo/detail.html', context)

