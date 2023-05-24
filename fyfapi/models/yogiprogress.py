from django.db import models


class YogiProgress(models.Model):
    user = models.ForeignKey(
        "Yogi", on_delete=models.CASCADE, related_name="userprogress")
    flow = models.ForeignKey(
        "Flow", on_delete=models.CASCADE, related_name="userprogress")
    date_completed = models.DateField()
