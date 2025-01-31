from django.shortcuts import render
from django.http import HttpResponse

def starting(request):

    return render(request, 'mysite/index.html')
    return HttpResponse('Stop this template madness, please!!!')

