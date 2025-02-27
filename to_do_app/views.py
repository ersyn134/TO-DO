from django.shortcuts import render ,get_object_or_404
from .models import Task

def index_view(request):
    return render(request, 'index.html')

def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})


def add_task_view(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status', 'new')
        date = request.POST.get('due_date')

        Task.objects.create(
            description=description,
            status=status,
            data=date,
        )

        tasks = Task.objects.all()
        return render(request, "tasks_list.html", {"tasks": tasks})

    return render(request, 'task_form.html')




def delete_task_view(request, task_id):
    task = Task.objects.filter(id=task_id).first()  # Ищем задачу, но не вызываем 404
    if task:
        task.delete()

    tasks = Task.objects.all()  # Получаем обновленный список задач
    return render(request, 'tasks_list.html', {'tasks': tasks})
