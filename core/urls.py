"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from to_do_app.views import task_list_view, add_task_view, index_view, delete_task_view, task_detail, task_list,task_api_detail

urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        "",
        index_view,
        name="index"),
    path(
        "list/",
        task_list_view,
        name="task_list"),
    path(
        "tasks/<int:task_id>/",
        task_detail,
        name="task_detail"),
    path(
        "tasks/add/",
        add_task_view,
        name="task_create"),
    path(
        "tasks/<int:task_id>/delete/",
        delete_task_view,
        name="delete_task"),

    path('api/tasks/', task_list, name='task_list_api'),
    path('api/tasks/<int:task_id>/', task_api_detail, name='task_detail_api'),
]
