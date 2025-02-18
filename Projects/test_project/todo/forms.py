from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from todo.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'desc', 'dead_line_dt']
        widgets = {
            "desc": forms.Textarea(attrs={"rows": 3}),
            "dead_line_dt": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }