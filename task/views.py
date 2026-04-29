from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskModelForm
from category.models import TaskCategory


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save()
            selected_categories = form.cleaned_data.get('categories')
            if selected_categories:
                for cat in selected_categories:
                    cat.tasks.add(task)
            return redirect('show_tasks')
    else:
        form = TaskModelForm()
    return render(request, 'task/add_task.html', {'form': form})


def edit_task(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            selected_categories = form.cleaned_data.get('categories', [])
            for cat in TaskCategory.objects.all():
                if cat in selected_categories:
                    cat.tasks.add(task)
                else:
                    cat.tasks.remove(task)
            return redirect('show_tasks')
    else:
        form = TaskModelForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form, 'task': task})


def delete_task(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('show_tasks')
    return render(request, 'task/confirm_delete.html', {'task': task})


def complete_task(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')
