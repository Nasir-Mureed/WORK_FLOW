from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
from django.utils.timezone import now
# Create your models here.
class Sprint(models.Model):
    name = models.CharField(max_length=100,unique=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    startDate = models.DateField(default=now)
    endDate = models.DateField()
    isActive = models.BooleanField(default=True)