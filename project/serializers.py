from rest_framework import serializers

from project.models import Project
from user.models import User
from user.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    '''
    Defines a serializer to Project Model to validate the data
    '''
    user_id = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'user_id']


class ProjectReadSerializer(serializers.ModelSerializer):
    '''
    Defines a serializer to read the Project Model to return to a get request
    '''
    user_id = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'user_id']
