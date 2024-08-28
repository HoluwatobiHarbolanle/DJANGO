from typing import Any
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .models import Task
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import RegisterForm, TaskForm
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.urls import reverse, reverse_lazy
"""
Class based views
"""
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


# Create your views here.
def index(request):
    return render(request, "base.html")

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            return render(request, 'register.html', {'error': 'Invalid form data', 'form': form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


class TaskList(ListView):
    model = Task, User
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    success_url = 'task_list'

    def get_queryset(self):
        # if self.request.user.is_superuser:
        #     return Task.objects.all()
        # else:
        usr = self.request.user
        return (Task.objects.filter(created_by = usr) or Task.objects.filter(assigned_to = usr).distinct()).order_by('created')
    def get_success_url(self):
        return reverse('task_list')

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'create-task.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm
    def form_valid(self, form):
        form.instance.created_by = self.request.user or self.request.user.is_superuser 
        form.instance.assigned_to =  self.request.user or self.request.user.is_supersuser
        return super().form_valid(form)
    def get_success_url(self) -> str:
        return reverse_lazy('task_list')
    
    # def get(self, request):
    #     task = Task.objects.create(
    #     title = request.POST.get('title'),
    #     complete = request.POST.get('status', 'off') == 'on',
    #     due_date = request.POST.get('datetime'),
    #     created_by = request.user,
    #     assigned_to = request.user
    #     )
    #     return redirect('task_list')
    
    # def post(self, request):
    #     return render(request, 'create-task.html')

class UpdateTask(UpdateView, UserPassesTestMixin):
    model = Task
    template_name = 'update_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def get_success_url(self):
        return reverse('task_list')
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.created_by or self.request.user.is_superuser



class DeleteTask(DeleteView, UserPassesTestMixin):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url=  reverse_lazy('task_list')
    context_object_name = 'task'
    def get_success_url(self):
        return reverse('task_list')
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.created_by or self.request.user.is_superuser
        

# def login(request):
#         login(request)
#         return redirect('task_list')


# def logout_view(request):
#     if request.method == 'POST':
#         auth_logout(request)
#     return render(request, 'logout.html')

#     # return render(request, 'logout.html')
# # def registration(request):
# #     if request.method == 'POST':
# #         username = request.POST.get('username')
# #         email = request.POST.get('email')
# #         password = request.POST.get('password1')
# #         confirm_password = request.POST.get('password2')
# #         if password == confirm_password:
# #             usr = User.objects.create_user(
# #                 username = username,
# #                 email = email,
# #                 password = password
# #             )
# #             return redirect('login')
# #         else:
# #             return render(request, 'registration.html', {'error': 'Passwords do not match.'})
# #     return render(request, 'registration.html')




# @login_required
# def task_lists(request):
#     u = request.user
#     # tasks = Task.objects.filter(Q(created_by = u) | Q(assigned_to = u))
#     tasks = (Task.objects.filter(created_by = u) or Task.objects.filter(assigned_to = u).distinct()).order_by('-created')

#     return render(request, "task_list.html", {"tasks": tasks, 'user':u})

# @login_required
# def create_new_task(request):
#     if request.method == 'POST':
#         task = Task.objects.create(
#             title = request.POST.get('title'),
#             complete = request.POST.get('complete', 'off') == 'on',
#             due_date = request.POST.get('due_date'),
#             created_by = request.user,
#             assigned_to = request.user
#         )
#         return redirect('task_list')
#     return render(request, 'create-task.html')

# @permission_required('can_edit_task')
# def update_task(request, task_id):
#     task = Task.objects.get(id=task_id)
#     if request.method == 'POST':
#         task.title = request.POST.get('title') 
#         task.complete = request.POST.get('complete') == 'on' 
#         task.due_date = request.POST.get('due_date')
#         task.save()
#         return redirect('task_list')
#     return render(request, 'update_task.html', {'task': task})


# @permission_required('can_delete_task')
# def delete_task(request, task_id):
#     task = Task.objects.get(id = task_id)
#     task.delete()
#     return redirect('task_list')
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