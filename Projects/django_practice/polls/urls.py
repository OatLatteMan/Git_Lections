from django.urls import path
from polls import views

urlpatterns = [
    path('indexx/', views.index, name='index'),
]

