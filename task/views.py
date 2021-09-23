from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .catSerializers import TaskCategorySerializer


# Create your views here.
@login_required(login_url='loginUser')
def todo(request):
    tasks = Task.objects.filter(user=request.user)

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            form.save()
        return redirect('todo')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'task/todo.html', context)

@login_required(login_url='loginUser')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo')

    context = {'form': form}

    return render(request, 'task/updateTodo.html', context)

@login_required(login_url='loginUser')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('todo')

    context = {'task': task}
    return render(request, 'task/delete.html', context)

@api_view(['GET', 'POST'])
def apiTasks(request):
    task = Task.objects.filter(user=request.user)
    serializer = TaskSerializer(task, many=True)

    return Response(serializer.data)

@api_view(['GET', 'POST'])
def apiTasksCategories(request):
    task = Task.objects.filter(user=request.user)
    serializer = TaskCategorySerializer(task, many=True)

    return Response(serializer.data)
