from django.contrib.auth.models import AbstractUser
from django.db import models

from user.managers import CustomUsermanager


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    login = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name', 'email']
    objects = CustomUsermanager()

    def __str__(self):
        return f'{self.login}'
