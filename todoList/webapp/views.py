from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from task.forms import TaskForm
from task.models import Task



def home(request):
    Task_number = Task.objects.count()
    tasks= Task.objects.all()
    return render(request, 'home.html', {'Task_number': Task_number, 'tasks': tasks})



def create(request):
    if request.method == 'POST':
        formTask = TaskForm(request.POST)
        if formTask.is_valid():
            formTask.save()
            return redirect('home')
    else:
        formTask = TaskForm()
    return render(request, 'create.html', {'formTask': formTask})