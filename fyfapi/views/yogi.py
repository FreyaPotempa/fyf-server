from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fyfapi.models import Yogi
from rest_framework.decorators import action


class YogiView(ViewSet):
    '''FYF user view'''

    def list(self, request):
        yogis = Yogi.objects.all()
        serializer = YogiSerializer(yogis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        yogi = Yogi.objects.get(pk=pk)
        serializer = YogiSerializer(yogi)
        return Response(serializer.data, status=status.HTTP_200_OK)


class YogiSerializer(serializers.ModelSerializer):
    '''JSON serializer for users'''
    class Meta:
        model = Yogi
        fields = ("id", "full_name",
                  "bio", "userPhoto", "isInstructor")
