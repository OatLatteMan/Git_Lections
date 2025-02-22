from django.shortcuts import render
from django.http import HttpResponse
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

    return render(request, 'final_project/tpcfuj.html', {'number': number})

