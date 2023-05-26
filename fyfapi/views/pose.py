from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fyfapi.models import Pose
from rest_framework.decorators import action


class PoseView(ViewSet):
    '''FYF pose view'''

    def list(self, request):
        poses = Pose.objects.all()
        serializer = PoseSerializer(poses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        pose = Pose.objects.get(pk=pk)
        serializer = PoseSerializer(pose)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PoseSerializer(serializers.ModelSerializer):
    '''JSON serializer for poses'''
    class Meta:
        model = Pose
        fields = ("id", "sanskrit_name", "english_name",
                  "img_url", "peak", "category")
