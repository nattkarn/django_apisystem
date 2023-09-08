from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add additional fields here
    pass

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField()

    class Meta:
        ordering = ['-date_created']
        db_table = 'task'
    
    def __str__(self):
        return self.title