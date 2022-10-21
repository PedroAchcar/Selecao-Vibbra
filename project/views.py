from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from project.models import Project

from project.serializers import ProjectReadSerializer, ProjectSerializer


class ProjectCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'project': serializer.data,
                'status': HTTP_201_CREATED
            })
        return Response({
            'message': serializer.errors,
            'status': HTTP_400_BAD_REQUEST
        })

    def get(self, request):
        try:
            projects = Project.objects.all()
            projects_serialized = ProjectReadSerializer(projects, many=True)
            return Response({
                'projects': projects_serialized.data,
                'status': HTTP_200_OK
            })

        except:
            return Response({
                'message': 'Some error occurred',
                'status': HTTP_400_BAD_REQUEST
            })


class ProjectDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
            serializer = ProjectReadSerializer(project)
            return Response({
                'project': serializer.data,
                'status': HTTP_200_OK
            })

        except Project.DoesNotExist:
            return Response({
                'message': 'Project not found',
                'status': HTTP_404_NOT_FOUND
            })

    def put(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
            serializer = ProjectSerializer(project, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'project': serializer.data,
                    'status': HTTP_200_OK
                })

        except Project.DoesNotExist:
            return Response({
                'message': 'Project not found',
                'status': HTTP_404_NOT_FOUND
            })
