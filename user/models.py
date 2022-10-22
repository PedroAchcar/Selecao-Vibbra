from django.contrib.auth.models import AbstractUser
from django.db import models

from user.managers import CustomUserManager


class User(AbstractUser):
    '''
    Model to define the User table at the database
    '''
    username = None
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    projects = models.ManyToManyField('project.Project')

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name', 'email', 'password']
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.login}'
