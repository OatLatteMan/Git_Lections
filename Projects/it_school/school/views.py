from django.shortcuts import render, HttpResponse, get_object_or_404
from school import models
from django.views import generic


def index(request):
    return render(request, 'school/index.html')

def students(request):
    return render(request, 'school/students.html')

def courses(request):
    courses = models.Course.objects.all()
    return render(request, 'school/courses.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)

    return render(request, 'school/course_detail.html', {'course': course})

class CourseDetail(generic.DetailView):
    model = models.Course

