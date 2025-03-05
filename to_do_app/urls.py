from django.urls import path
from to_do_app.views import TaskDetailView, TaskListView, TaskCreateView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),   # GET /api/tasks/ - список задач
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),  # GET /api/tasks/1/ - детальная информация
    path('tasks/add/', TaskCreateView.as_view(), name='task-create'),  # POST /api/tasks/add/ - создание задачи
]
