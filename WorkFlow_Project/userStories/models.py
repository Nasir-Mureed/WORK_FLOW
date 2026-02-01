from django.db import models
from sprints.models import Sprint
# Create your models here.

class UserStory(models.Model):
    description=models.CharField(max_length=200)
    sprint=models.ForeignKey(Sprint,on_delete=models.CASCADE)

    def __str__(self):
        return self.description