from django import forms
from task.models import Task


class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = [
            'name',
            'startTime',
            'endTime',
        ]
        labels = {
            'name' : 'Nombre',
            'startTime': 'Hora de inicio',
            'endTime': 'Hora final',
        }
        widgets = {
            'name': forms.TextInput(),
            'startTime': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'endTime': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
