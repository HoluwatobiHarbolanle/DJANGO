from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.registration, name= 'register'),
    path('login', views.login, name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    path('task_list', views.TaskList.as_view(), name='task_list'),
    path('create_task/', views.CreateTask.as_view(), name='create_task'),
    path('update_task/<int:pk>/', views.UpdateTask.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', views.DeleteTask.as_view(), name='delete_task'),

    path('account/password_reset/', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset.html'), name='password_reset'),
    path('account/password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'), name='password_reset_done'),
    path('account/password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('account/password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'), name='password_reset_complete')
]


    # path('create_task/', views.create_new_task, name='create_task'),
    # path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    # path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),