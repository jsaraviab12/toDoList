from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    startTime = models.TimeField()
    endTime = models.TimeField()

class Historial(models.Model):
    name = models.CharField(max_length=255)
    startTime = models.TimeField()
    endTime = models.TimeField()
    task = models.ForeignKey(Task, on_delete= models.SET_NULL, null= True)
