from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
# LIST
def task_list(request):
    tasks = Task.objects.all().order_by('-id')  # Optional: latest first
    return render(request, 'app/task_list.html', {'tasks': tasks})

# CREATE
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'app/task_form.html', {'form': form})

# UPDATE
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)
    return render(request, 'app/task_form.html', {'form': form})

# DELETE
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'app/task_confirm_delete.html', {'task': task})