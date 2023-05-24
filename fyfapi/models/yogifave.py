from django.db import models


class YogiFave(models.Model):
    user = models.ForeignKey(
        "Yogi", on_delete=models.CASCADE, related_name="favoriteflow")
    flow = models.ForeignKey(
        "Flow", on_delete=models.CASCADE, related_name="userfave")
