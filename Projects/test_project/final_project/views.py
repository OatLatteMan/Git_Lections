from django.shortcuts import render
from django.http import HttpResponse

# function index()
def index(request, number):
    context = {
        'number': number,
    }

    return render(request, 'final_project/tpcfuj.html', context)

