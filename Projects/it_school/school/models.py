from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    image = models.ImageField(blank=True, null=True, upload_to='course/')

    lector = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='lector_courses')

    students = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("school:course_detail", kwargs={"pk": self.pk})

