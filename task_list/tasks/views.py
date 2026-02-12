from django.shortcuts import render, redirect
from .models import TaskList
from .forms import AddTask

def home(request):
    tasks = TaskList.objects.all()
    form = AddTask()
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')        
    context = {'form':form, 'tasks':tasks}
    return render(request, 'home.html', context)

def edit(request, task_id):
    task = TaskList.objects.get(id=task_id)
    task.done = True
    task.save()
    return redirect('home')

def delete(request, task_id):
    task = TaskList.objects.get(id=task_id)
    task.delete()
    return redirect('home')
