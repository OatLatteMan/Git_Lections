from django.urls import path
from final_project import views

app_name = 'final_project'

urlpatterns = [
    path('<int:number>/', views.index, name='index'),
]

