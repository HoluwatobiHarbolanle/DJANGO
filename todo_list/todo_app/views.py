from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def index(request):
    return render(request, "base.html")

def task_lists(request):
    tasks = Task.objects.all()

    return render(request, "task_list.html", {"tasks": tasks})