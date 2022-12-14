from django.db import models


class Project(models.Model):
    '''
    Model to define the Project table at the database
    '''
    title = models.CharField(max_length=255)
    description = models.TextField()

    user_id = models.ManyToManyField('user.User')

    def __str__(self):
        return f'{self.title}'
