from django.contrib import admin

# Register your models here.
from task.models import Task, Historial

admin.site.register(Task)
admin.site.register(Historial)