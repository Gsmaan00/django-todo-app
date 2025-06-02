from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Task
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='login')
def index(request):
    # tasks = Task.objects.all()
    tasks = Task.objects.filter(user=request.user)
    # logger.debug(f"Retrieved tasks: {tasks}")
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title, user=request.user)
        # logger.info(f"Created new task: {title}")
        return redirect('/')
    return render(request, 'todo/index.html', {'tasks': tasks})

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    # logger.info(f"Deleted task: {task.title}")
    return redirect('/')

def toggle_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # logger.info(f"User registered: {user.username}")
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})
