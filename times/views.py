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
from user.models import User
from times.models import Time
from times.serializers import TimeSerializer


class TimeCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user = User.objects.get(id=request.data['user_id'])
            project = Project.objects.get(id=request.data['project_id'])

            data = {
                "started_at": request.data['started_at'],
                "ended_at": request.data['ended_at']
            }

            serializer = TimeSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                time = Time.objects.get(
                    started_at=request.data['started_at'],
                    ended_at=request.data['ended_at']
                )
                time.user = user
                time.project = project
                time.save()

                return Response({
                    'time': {
                        'id': time.id,
                        'started_at': time.started_at,
                        'ended_at': time.ended_at,
                        'project_id': request.data['project_id'],
                        'user_id': request.data['user_id']
                    },
                    'status': HTTP_201_CREATED
                })

        except User.DoesNotExist:
            return Response({
                'message': 'User not found',
                'status': HTTP_404_NOT_FOUND
            })

        except Project.DoesNotExist:
            return Response({
                'message': 'Project not found',
                'status': HTTP_404_NOT_FOUND
            })

        except:
            return Response({
                'message': 'Some error occurred',
                'status': HTTP_400_BAD_REQUEST
            })


class TimeDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        times = Time.objects.filter(id=id)
        serializer = TimeSerializer(instance=times, many=True)
        return Response({
            'time': serializer.data,
            'status': HTTP_200_OK
        })

    def put(self, request, id):
        try:
            time = Time.objects.get(id=id)
            serializer = TimeSerializer(instance=time, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'time': serializer.data,
                    'status': HTTP_200_OK
                })

        except Time.DoesNotExist:
            return Response({
                'message': 'Time not found',
                'status': HTTP_404_NOT_FOUND
            })

        except:
            return Response({
                'erros': serializer.errors
            })
