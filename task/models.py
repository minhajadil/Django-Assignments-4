from django.db import models
# Create your models here.
from category.models import TaskCategory

class TaskModel(models.Model):
    task_Title= models.CharField(max_length=40)
    task_Description= models.TextField()
    category =models.ManyToManyField(TaskCategory)
    is_Completed =models.BooleanField(default=False)
    Task_Assign_date = models.DateField()
    
    
    def __str__(self):
        return self.task_Title


