from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from todo_app.models import Task
from .serializers import TaskSerializer

router = DefaultRouter()
router.register('tasklist', views.TaskListView, basename= 'tasklist')

urlpatterns = [
    path('', views.TaskListView.as_view()), #queryset=Task.objects.all(), serializer_class = TaskSerializer)
    path('retrieve-update-destroy/<int:pk>/', views.RetrieveUpdateDestroyTaskView.as_view(), name= 'retriveUpdateDestroy')
    # path('', router.urls) for a viewset
]