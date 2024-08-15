from django.shortcuts import redirect, render
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "base.html")

@login_required
def task_lists(request):
    tasks = Task.objects.all()

    return render(request, "task_list.html", {"tasks": tasks})

def create_new(request):
    if request.method == 'POST':
        task = Task(
            title = request.POST.get('title'),
            complete = request.POST.get('status', 'off') == 'on',
            due_date = request.POST.get('datetime')
        )
        task.save()
        return redirect('task_list')
    return render(request, 'create-task.html')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title') 
        task.complete = request.POST.get('status') == 'on' 
        task.due_date = request.POST.get('datetime')
        task.save()
        return redirect('task_list')
    return render(request, 'update_task.html', {'task': task})


def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('task_list')
    # return render(request, 'task_list.html')

"""
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST) submit the form data with the model instance.
        if form.is_valid()
            form.save()
            return redirect('task_list')

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        
"""