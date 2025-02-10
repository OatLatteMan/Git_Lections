from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # http://127.0.0.1:2091/polls/tester
    path('indexes/', views.indexes, name='indexes'),

    # http://127.0.0.1:2091/polls/
    path("", views.IndexView.as_view(), name="index"),

    # http://127.0.0.1:2091/polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # http://127.0.0.1:2091/polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # http://127.0.0.1:2091/polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

