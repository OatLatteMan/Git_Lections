from django.urls import path
from school import views

app_name = 'school'

urlpatterns = [
    path('index/', views.index, name='index')
]
