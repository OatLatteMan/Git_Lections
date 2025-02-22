from django.shortcuts import render
from django.http import HttpResponse


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


def home(request, number):
    context = {
        'number': number,
    }

    return render(request, 'final_project/tpcfuj.html', context)

