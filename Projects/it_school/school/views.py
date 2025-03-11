from django.shortcuts import render, HttpResponse, get_object_or_404
from school import models


def index(request):
    return render(request, 'school/index.html')

def students(request):
    return render(request, 'school/students.html')

def courses(request):
    courses = models.Course.objects.all()
    return render(request, 'school/courses.html', {'courses': courses})

def course_details(request, pk):
    course = get_object_or_404(models.Course, pk=pk)

    return render(request, 'school/course_details.html', {'course': course})

