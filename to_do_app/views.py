from django.shortcuts import render, get_object_or_404, redirect, reverse
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task


@csrf_exempt
def task_list(request):
    if request.method == "GET":
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            task = Task.objects.create(
                title=data.get("title", ""),
                description=data.get("description", ""),
                status=data.get("status", "pending"),
                due_date=data.get("due_date", None)
            )
            return JsonResponse(
                {"id": task.id, "message": "Task created"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
def task_api_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)

    if request.method == "GET":
        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "due_date": task.due_date.strftime("%Y-%m-%d") if task.due_date else None
        })

    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            task.title = data.get("title", task.title)
            task.description = data.get("description", task.description)
            task.status = data.get("status", task.status)
            task.due_date = data.get("due_date", task.due_date)
            task.save()
            return JsonResponse({"message": "Task updated"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == "DELETE":
        task.delete()
        return JsonResponse({"message": "Task deleted"}, status=204)


def index_view(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {"tasks": tasks})


def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, "task_detail.html", {"task": task})


def add_task_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status', 'new')
        date = request.POST.get('due_date')

        Task.objects.create(
            description=description,
            status=status,
            due_date=date,
            title=title
        )

        tasks = Task.objects.all()
        return redirect(reverse('task_list'))

    return render(request, 'task_form.html')


def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect(reverse('task_list'))
