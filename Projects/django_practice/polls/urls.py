from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    # http://127.0.0.1:2091/polls/tester
    path('indexes/', views.indexes, name='indexes'),

    # http://127.0.0.1:2091/polls/
    path('', views.index, name='index'),

    # http://127.0.0.1:2091/5/
    path("<int:question_id>/", views.detail, name="detail"),

    # http://127.0.0.1:2091/5/results/
    path("<int:question_id>/results/", views.results, name="results"),

    # http://127.0.0.1:2091/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

