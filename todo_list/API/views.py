from django.shortcuts import render
from todo_app.models import Task
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView

# Create your views here.

class TaskListView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes =[permissions.IsAuthenticated]

