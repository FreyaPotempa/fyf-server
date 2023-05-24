from django.db import models
from django.contrib.auth.models import User


class Yogi(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    isInstructor = models.BooleanField(default=False)
    userPhoto = models.URLField(max_length=250)
