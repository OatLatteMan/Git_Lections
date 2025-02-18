from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Task, Register
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from todo.forms import TaskForm

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

        if task.user == request.user:
            if request.method == 'POST':
                form = TaskForm(request.POST, instance=task)
                if form.is_valid():
                    form.save()
                    return redirect('/todo/list/')
            else:
                form = TaskForm(instance=task)
            return render(request, 'todo/detail.html', {'task': task, 'form': form})
    return redirect('/todo/')

def todo_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskForm(request.POST)

            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()
                print(task, task.id)
                return redirect('/todo/list/') # todo: opravit
        else:
            form = TaskForm()

        return render(request, 'todo/new.html', {'form': form})
    else:
        return redirect('/todo')

def todo_task_delete(request, number):
    """
    1) Find the task
      - by number "id = number"
      - user must be authenticated
      - task must belong to specified user
    2) Delete the task by id
    3) Show the list
    """
    if request.method == 'POST':
        if request.user.is_authenticated:
            task = get_object_or_404(Task, id=number, user=request.user)
            task.delete()
            return redirect('/todo/list/')

    return redirect('/todo/')

def todo_task_finish(request, number):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=number, user=request.user)
        if task.is_finished == False:
            task.is_finished = True
            task.save()
        else:
            task.is_finished = False
            task.save()
        return redirect('/todo/list/')

    return redirect('/todo/')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return redirect('/todo/list')
        else:
            form = RegisterForm(request.POST)
            login = request.POST.get('login', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            user = User.objects.create_superuser(username=login, password=password, email=email)
            user.is_staff = True
            user.save()
            return render(request, 'todo/list.html', {'form': form})
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

