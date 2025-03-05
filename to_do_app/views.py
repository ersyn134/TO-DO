from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Task


class TaskDetailView(APIView):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        return Response({
            'id': task.id,
            'title': task.title,
            'description': task.description or "No description",
            'status': task.status,
            'date': task.due_date.isoformat() if task.due_date else None
        }, status=status.HTTP_200_OK)

    def put(self, request, id):
        task = get_object_or_404(Task, id=id)

        title = request.data.get('title', task.title)
        description = request.data.get('description', task.description)
        status_value = request.data.get('status', task.status)
        due_date = request.data.get('date', task.due_date)

        if due_date:
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                return Response(
                    {'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        task.title = title
        task.description = description
        task.status = status_value
        task.due_date = due_date
        task.save()

        return Response({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'date': task.due_date.isoformat() if task.due_date else None
        }, status=status.HTTP_200_OK)

    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response({'message': 'Task deleted successfully'},
                        status=status.HTTP_204_NO_CONTENT)


class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        task_list = [{
            'id': task.id,
            'title': task.title,
            'description': task.description or "No description",
            'status': task.status,
            'date': task.due_date.isoformat() if task.due_date else None
        } for task in tasks]

        return Response(task_list, status=status.HTTP_200_OK)


class TaskCreateView(APIView):
    def post(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        status_value = request.data.get('status', 'new')
        due_date = request.data.get('date')

        if not title or not description or not status_value:
            return Response({'error': 'All fields are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if due_date:
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                return Response(
                    {'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        task = Task.objects.create(
            title=title,
            description=description,
            status=status_value,
            due_date=due_date
        )

        return Response({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'date': task.due_date.isoformat() if task.due_date else None
        }, status=status.HTTP_201_CREATED)


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
