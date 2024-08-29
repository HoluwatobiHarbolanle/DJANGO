from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListView
from todo_app.models import Task
from .serializers import TaskSerializer

router = DefaultRouter()
router.register('tasklist', TaskListView, basename= 'tasklist')

urlpatterns = [
    path('', TaskListView.as_view()), #queryset=Task.objects.all(), serializer_class = TaskSerializer)
    # path('', router.urls) for a viewset
]