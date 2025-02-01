from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    # return HttpResponse('Greetings for Dima')
    return render(request, 'polls/index.html')

