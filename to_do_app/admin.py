from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','status','due_date')
    search_fields = ('title','description', 'status', 'due_date')
    ordering = ('status',)
