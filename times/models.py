from django.db import models


class Time(models.Model):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    project = models.ForeignKey('project.Project',  models.CASCADE, null=True)
    user = models.ForeignKey('user.User',  models.CASCADE, null=True)

    def __str__(self):
        return f'Project {self.project} - User {self.user.name}'
