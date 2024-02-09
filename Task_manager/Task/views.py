from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .forms import RegistrationsFrom, TaskForm
from django.contrib import messages
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


class LandingPageView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)


class RegistrationView(View):
    def get(self, request):
        form = RegistrationsFrom()
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)

    def post(self, request):
        form = RegistrationsFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! Registration Successfully!')
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)


class TaskListView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.all().order_by('priority')
        context = {
            'tasks': tasks,
        }
        return render(request, 'task_list.html', context)


class TaskCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_creation.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.creator = request.user
            task.save()
            messages.add_message(request, messages.SUCCESS, 'Congratulations! Task created successfully.')
            return redirect(reverse('task-list'))
        else:
            messages.error(request, 'Error submitting the form. Please check your inputs.')
            print(form.errors)  # Print form errors for debugging purposes
            print(request.POST)
        return render(request, 'task_creation.html', {'form': form})




class TaskDetailView(LoginRequiredMixin, View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task = Task.objects.get(pk=task_id)
        return render(request, 'task_details.html', {'task': task})


class TaskUpdateView(LoginRequiredMixin, View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(instance=task)
        return render(request, 'task_update.html', {'form': form, 'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            if 'new_photo' in request.FILES:
                new_photo = request.FILES['new_photo']
                task.photo = new_photo
            form.save()
            return redirect(reverse('task-list'))
        return render(request, 'task_update.html', {'form': form, 'task': task})


class TaskDeleteView(LoginRequiredMixin, View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        return render(request, 'task_delete_confirm.html', {'task': task})

    def post(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        task.delete()
        return redirect(reverse('task-list'))


class SearchItemView(View):
    template_name = 'search.html'

    def get(self, request):
        query = request.GET.get('query')
        if query:
            task = Task.objects.filter(Q(title__icontains=query))
            return render(request, self.template_name, {'task': task})
        else:
            return render(request, self.template_name, {'message': 'Sorry!! No Match!'})
