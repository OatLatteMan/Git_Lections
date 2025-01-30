from django.http import HttpResponse
from django.shortcuts import render
import random
import datetime as dt

# Create your views here.


def index_page(request):
    print(vars(request))
    number = random.randint(1, 100)
    d = dt.datetime.now()
    return HttpResponse(f'<h1>Hello <br>from<br> Vysocany: {number} | {d}</h1><br><img src="https://picsum.photos/200/300">')

def url_paths(request):

    print(request.GET)
    print(request.GET['xyz'])
    print(request.GET.getlist('xyz'))
    # ?key=value&xyz=10&xyz=20

    return HttpResponse('This page is working. COYS!')

def my_math(request):

    """
    ?operation=plus&a=10&b=100
    operation=plus, minus, multiply, divide
    a=prvni cislo
    b=druhe cislo
    """

    a = int(request.GET['a'])
    b = int(request.GET['b'])
    operation = request.GET['operation']
    print(operation, a, b)

    if operation == 'plus':
        result = a + b
    elif operation == 'minus':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = int(a / b)

    return HttpResponse(f'Result = {result}')

# MVT - model view template (HTML šablona)
# MVC - model view controller (ovladač)

def test_template(request):
    name = request.GET.get('name', 'world')
    age = int(request.GET['age'])

    """
    try:
        name = request.GET['name']
    except KeyError:
        name = 'world'
    """

    context = {
        'date': dt.datetime.now(),
        'name': name,
        'age': age
        }

    return render(request, 'myapp/test_template.html', context)

def calculator(request):

    try:
        operation = request.GET['operation']
        a = int(request.GET['a'])
        b = int(request.GET['b'])

        if operation == 'plus':
            result = a + b
        elif operation == 'minus':
            result = a - b
        elif operation == 'multiple':
            result = a * b
        elif operation == 'divide':
            result = a / b

    except (KeyError, TypeError, ValueError):
        result = ''
    except ZeroDivisionError:
        result = ''

    context = {
        'result': result
    }

    return render(request, 'myapp/calculator.html', context)

def age(request):
    try:
        a = int(request.GET['a'])
        actual_age = 2025 - a

    except (KeyError, TypeError, ValueError):
        a = None
        actual_age = '"Not defined yet"'

    context = {
        'a': a,
        'actual_age': actual_age,
    }

    return render(request, 'myapp/age.html', context)

# def _time(request):
#     date = dt.datetime.now().strftime("%d.%m.%Y")
#     time = dt.datetime.now().strftime("%H:%M:%S")
#     return HttpResponse(date + "<br><br>" + time)

def _time(request):
    date = dt.datetime.now().strftime("%d.%m.%Y")
    time = dt.datetime.now().strftime("%H:%M:%S")

    context = {
        'date': date,
        'time': time,
    }

    return render(request, 'myapp/time.html', context)

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    print(username, password)
    print(request.FILES, '<<<<<< FILES')

    if username == '15minstan@gmail.com':
        return render(request, 'login_success.html')

    # print(request._body)
    # print(request.POST)

    return render(request, 'myapp/login.html')

def my_page(request, name):


    return render(request, 'myapp/my_page.html', {'name': name})

def signup(request):
    password = request.POST.get('pass')
    password_repeat = request.POST.get('pass_rep')

    if password:
        if password != password_repeat:
            return render(request, 'myapp/signup_failed.html')
        elif password == password_repeat:
            return render(request, 'myapp/signup_success.html')


    return render(request, 'myapp/signup.html')

def article(request, name, number):


    return HttpResponse(
        f"""
        <h1>{name} - {number}</h1>
        """
    )

def pages(request, number, name):

    return HttpResponse(
        f"""
        <h1>Number is: {number}, name is: {name}</h1>
        """
    )

