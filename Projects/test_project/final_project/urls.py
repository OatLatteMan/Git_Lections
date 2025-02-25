from django.urls import path
from final_project import views

app_name = 'final_project'

urlpatterns = [
    # http://127.0.0.1:[PORT]/final_project
    path('', views.home, name='home'),

    # http://127.0.0.1:[PORT]/final_project/films
    path('films/', views.films, name='films'),

    # http:127.0.0.1:[PORT]/final_project/serials
    path('serials/', views.serials, name='serials'),

    # http://127.0.0.1:[PORT]/final_project/actors
    path('actors/', views.actors, name='actors'),
]

