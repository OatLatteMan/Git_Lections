from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from final_project.models import ItemType, Genre, Item, Review

"""
Tabs:
    - Home (about)
    - Films and serials (detail)
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

"""
Questions to ask:
    - Better to make united page for films and serials, or two separated? - United
    - If users are creating reviews, how do we tell django, that a certain
      user is logged in? - Make reviews from different web-browsers or inkognito tabs
    - How to upload on server if I need to run "runserver" every time? - We'll do it together and make that work non-stop
"""


def home(request):
    return render(request, 'final_project/home.html')

def films_serials(request):
    return render(request, 'final_project/films_serials.html')

def actors(request):
    return render(request, 'final_project/actors.html')

def detail(request, number):
    return render(request, 'final_project/detail.html', {'number': number})

def final_project_new(request):

    return render(request, 'final_project/new.html')