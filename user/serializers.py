from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    '''
    Defines a serializer to User Model to validate the data
    '''
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'login', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        '''
        Default create function was alterated to set the password with criptography
        '''
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class TokenObtainLifetimeSerializer(TokenObtainPairSerializer):
    '''
    Defines a serializer to obtain the JWT Token and add to the response data the user object
    '''

    def validate(self, attrs):
        data = super().validate(attrs)
        user = User.objects.get(id=self.user.id)
        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "login": user.login
        }
        data['user'] = user_data
        return data
