from django.urls import path
from todo import views

app_name = 'todo'

"""
/todo/
/todo/list/
/todo/new/
/todo/7627/
"""

urlpatterns = [
    # http://127.0.0.1:[PORT]/todo
    path('', views.index, name='index'),

    # http://127.0.0.1:[PORT]/todo/list
    path('list/', views.todo_list, name='list'),

    # http://127.0.0.1:[PORT]/todo/new
    path('new/', views.todo_new, name='new'),

    # http://127.0.0.1:[PORT]/todo/register
    path('register/', views.register, name='register'),

    # http://127.0.0.1:[PORT]/todo/detail
    path('<int:number>/', views.todo_detail, name='detail'),

    # http://127.0.0.1:[PORT]/todo/detail/delete
    path('<int:number>/delete/', views.todo_task_delete, name='task_delete'),

    # http://127.0.0.1:[PORT]/todo/detail/finish
    path('<int:number>/finish/', views.todo_task_finish, name='task_finish'),

]