from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    image = models.ImageField(blank=True, null=True, upload_to='course/')

    lector = models.ForeignKey(User, )

    def __str__(self):
        return self.name
