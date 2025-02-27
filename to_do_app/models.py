from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]

    title = models.TextField(max_length=2000,null=True,blank=True)
    description = models.TextField(max_length=2000,null=False,blank=False)
    status = models.CharField(max_length=20,null=False,blank=False,default='new',choices=STATUS_CHOICES)
    due_date = models.DateField(null=True,blank=True,default=None)