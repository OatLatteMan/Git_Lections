from django.urls import path
from todo import views

app_name = 'final_project'

urlpatterns = [
    path('<int:number>', views.index, name='index'),
]


