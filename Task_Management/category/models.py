from django.db import models
# from task.models import TaskModel

# Create your models here.

class TaskCategory(models.Model):
    Category_Name = models.CharField(max_length=40)
    # task = models.ManyToManyField(TaskModel)

    def __str__(self):
        return self.Category_Name
