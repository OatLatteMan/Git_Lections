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

    return render(request, 'test_template.html', context)

def calculator(request):
    try:
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        result = a + b
    except (KeyError, TypeError, ValueError):
        result = ''

    context = {
        'result': result
    }

    return render(request, 'calculator.html', context)

