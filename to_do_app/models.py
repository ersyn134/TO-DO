from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]

    title = models.TextField(max_length=2000, null=False, blank=False,default='No title')
    description = models.TextField(max_length=2000, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        null=False,
        blank=False
    )
    due_date = models.DateField(null=True, blank=True)
