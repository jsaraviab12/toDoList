from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    startTime = models.CharField(max_length=255)
    endTime = models.CharField(max_length=255)
