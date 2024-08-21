from django.shortcuts import redirect, render
from .models import Task
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def index(request):
    return render(request, "base.html")

def login(request):
        login(request)
        return redirect('task_list')


def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
    return render(request, 'logout.html')

    # return render(request, 'logout.html')
# def registration(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password1')
#         confirm_password = request.POST.get('password2')
#         if password == confirm_password:
#             usr = User.objects.create_user(
#                 username = username,
#                 email = email,
#                 password = password
#             )
#             return redirect('login')
#         else:
#             return render(request, 'registration.html', {'error': 'Passwords do not match.'})
#     return render(request, 'registration.html')

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Invalid form data', 'form': form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


@login_required
def task_lists(request):
    u = request.user
    tasks = Task.objects.filter(Q(created_by = u) & Q(assigned_to = u))

    return render(request, "task_list.html", {"tasks": tasks})

@login_required
def create_new_task(request):
    if request.method == 'POST':
        task = Task.objects.create(
            title = request.POST.get('title'),
            complete = request.POST.get('status', 'off') == 'on',
            due_date = request.POST.get('datetime'),
            created_by = request.user,
            assigned_to = request.user
        )
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