from django.shortcuts import render
from django.http import HttpResponse

"""
Films:
    - Inception
    - Interstellar
    - 50 shades of gray
"""

# function index()
def index(request, number):
    context = {
        'number': number,
    }

    return render(request, 'final_project/tpcfuj.html', context)

