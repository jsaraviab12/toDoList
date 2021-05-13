from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from task.forms import TaskForm
from task.models import Task, Historial


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

def edit(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        formTask = TaskForm(request.POST, instance=task)
        if formTask.is_valid():
            formTask.save()
            return redirect('home')
    else:

        formTask = TaskForm(instance=task)
    return render(request, 'edit.html', {'formTask': formTask})

def delete(request, id):
    task = get_object_or_404(Task, pk=id)
    if task:
        task.delete()
    return redirect('home')

def history(request):
    history_number = Historial.objects.count()
    return render(request, 'history.html', {'history_number': history_number})
