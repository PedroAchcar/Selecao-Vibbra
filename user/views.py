from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)

from user.models import User
from user.serializers import UserSerializer, TokenObtainLifetimeSerializer


class UserCreateView(APIView):
    '''
    Defines a view for the creation (POST) of a user
    '''
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'user': serializer.data,
                'status': HTTP_201_CREATED
            })
        return Response({
            'message': serializer.errors,
            'status': HTTP_400_BAD_REQUEST
        })


class UserDetailView(APIView):
    '''
    Defines a view for the details of one user (GET) or edit one user that already exists (PUT)
    '''
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        '''
        Pk (Personal Key) here is the ID of the user to get the details of it
        '''
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response({
                'user': serializer.data,
                'status': HTTP_200_OK
            })

        except User.DoesNotExist:
            return Response({
                'message': 'User not found',
                'status': HTTP_404_NOT_FOUND
            })

    def put(self, request, pk):
        '''
        Pk (Personal Key) here is the ID of the user to edit it
        '''
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'user': serializer.data,
                    'status': HTTP_200_OK
                })

        except User.DoesNotExist:
            return Response({
                'message': 'User not found',
                'status': HTTP_404_NOT_FOUND
            })


class TokenObtainPairView(TokenViewBase):
    '''
    View that serializes the data of the login/password to generate the proper response
    '''
    serializer_class = TokenObtainLifetimeSerializer
