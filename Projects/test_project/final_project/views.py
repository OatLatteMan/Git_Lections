from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

import random


"""
Tabs:
    - Home (about)
    - Films
    - Serials
    - Actors

Films:
    - Inception
    - Interstellar
    - 50 shades of gray

Serials:
    - Friends
    - Gotham
    - The Witcher
"""


def home(request):
    number = random.randint(1, 100)

    return render(request, 'final_project/home.html', {'number': number})

def films(request):
    return render(request, 'final_project/films.html')

def serials(request):
    return render(request, 'final_project/serials.html')

def actors(request):
    return render(request, 'final_project/actors.html')

