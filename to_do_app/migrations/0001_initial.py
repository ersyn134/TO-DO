# Generated by Django 5.1.6 on 2025-02-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=2000, null=True)),
                ('description', models.TextField(max_length=2000)),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('completed', 'Завершена')], default='new', max_length=20)),
                ('due_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
    ]
