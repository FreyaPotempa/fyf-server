from django.db import models


class Flow(models.Model):
    title = models.CharField(max_length=50)
    poseColumnIdList = models.ManyToManyField("Pose", related_name="flow")
    user = models.ForeignKey(
        "Yogi", on_delete=models.CASCADE, related_name="created_flows")
    difficulty = models.IntegerField()
