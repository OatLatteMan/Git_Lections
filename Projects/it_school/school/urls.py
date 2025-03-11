from django.urls import path
from school import views

app_name = 'school'

urlpatterns = [
    # http://127.0.0.1:[PORT]/school/index
    path('index/', views.index, name='index'),

    # http://127.0.0.1:[PORT]/school/courses
    path('courses/', views.courses, name='courses'),

    # http://127.0.0.1:[PORT]/school/courses_details
    path('courses/<int:pk>', views.course_details, name='course_details'),

    # http://127.0.0.1:[PORT]/school/students
    path('students/', views.students, name='students'),
]
