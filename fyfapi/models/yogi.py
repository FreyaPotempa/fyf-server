from django.db import models
from django.contrib.auth.models import User


class Yogi(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    userPhoto = models.URLField(max_length=250)
    isInstructor = models.BooleanField(default=False)

    @property  # decorator
    def full_name(self):
        """Additional field to capture from the client"""
        return f'{self.user.first_name} {self.user.last_name}'
