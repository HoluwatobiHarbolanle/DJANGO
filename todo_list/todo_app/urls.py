from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index, name='index'),
    path('', views.registration, name= 'register'),
    path('task_list', views.task_lists, name='task_list'),
    path('create_task', views.create_new_task, name='create_task'),
    path('update_task/<int:task_id>', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
]