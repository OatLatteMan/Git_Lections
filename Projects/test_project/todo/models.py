from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    is_finished = models.BooleanField(default=False)
    finished_dt = models.DateTimeField(blank=True, null=True)
    dead_line_dt = models.DateTimeField(blank=True, null=True)

    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    login = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=96)

    def __str__(self):
        return self.email

