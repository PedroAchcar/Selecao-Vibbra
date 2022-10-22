from enum import unique
from django.db import models


class Time(models.Model):
    '''
    Model to define the Time table at the database
    '''
    started_at = models.DateTimeField(unique=True)
    ended_at = models.DateTimeField(unique=True)

    project = models.ForeignKey('project.Project',  models.CASCADE, null=True)
    user = models.ForeignKey('user.User',  models.CASCADE, null=True)

    def __str__(self):
        return f'Project {self.project} - User {self.user.name}'
