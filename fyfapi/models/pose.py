from django.db import models


class Pose(models.Model):

    sanskrit_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    img_url = models.URLField(max_length=250)
    peak = models.BooleanField(default=False)
    category = models.CharField(max_length=50, default="uncategorized")
