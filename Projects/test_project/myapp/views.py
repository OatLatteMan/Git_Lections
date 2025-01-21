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

