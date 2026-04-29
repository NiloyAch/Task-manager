from django.db import models
from task.models import TaskModel


class TaskCategory(models.Model):
    categoryName = models.CharField(max_length=100)
    tasks = models.ManyToManyField(TaskModel, blank=True)

    def __str__(self):
        return self.categoryName

    class Meta:
        verbose_name_plural = "Task Categories"
