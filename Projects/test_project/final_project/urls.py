from django.urls import path
from final_project import views

app_name = 'final_project'

urlpatterns = [
    path('', views.home, name='home'),

]

