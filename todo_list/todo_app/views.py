from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def index(request):
    return render(request, "base.html")

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
    task = Task.objects.get(id= task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title'),
        task.complete = request.POST.get('status'),
        task.due_date = request.POST.get('datetime')
        # task.complete = complete
        if 'status' in request.POST:
            task.complete = True
        else:
            task.complete = False
        print(task.complete)
        task.save()
        return redirect('task_list')
    return render(request, 'update_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('task_list')
    # return render(request, 'task_list.html')