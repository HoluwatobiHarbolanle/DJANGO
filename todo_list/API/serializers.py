from todo_app.models import Task, User
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
    