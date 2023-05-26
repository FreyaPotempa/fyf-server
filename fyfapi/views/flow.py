from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fyfapi.models import Flow, Yogi, Pose
from rest_framework.decorators import action


class FlowView(ViewSet):
    '''FYF flow view'''

    def list(self, request):
        flows = Flow.objects.all()
        serializer = FlowSerializer(flows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        flow = Flow.objects.get(pk=pk)
        serializer = FlowSerializer(flow)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        yogi = Yogi.objects.get(user=request.auth.user)
        serializer = CreateFlowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=yogi)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        flow = Flow.objects.get(pk=pk)
        flow.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


@action(methods=['post'], detail=True)
def pose_flow(self, request, pk):
    '''POST request to add a pose to a flow'''
    pose = Pose.objects.get(request.data['pose'][id])
    flow = Flow.objects.get(pk=pk)
    flow.poseColumnIdList.add(pose)
    return Response({'message': 'pose added'}, status=status.HTTP_201_CREATED)


class CreateFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flow
        fields = (
            "id",
            "title",
            "poseColumnIdList", "difficulty"
        )


class PoseColumnSerializer(serializers.ModelSerializer):
    '''JSON serializer for poses in flow'''
    class Meta:
        model = Pose
        fields = ("id")


class FlowSerializer(serializers.ModelSerializer):
    '''JSON serializer for flows'''

    poseColumnIdList = PoseColumnSerializer(many=True)

    class Meta:
        model = Flow
        fields = ("id", "title", "poseColumnIdList", "user", "difficulty")
        depth = 1
