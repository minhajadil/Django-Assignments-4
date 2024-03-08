from django import forms
from task.models import TaskModel
from category.models import TaskCategory
class TaskForm(forms.ModelForm):
    class Meta:
        model =TaskModel
        fields='__all__'

        

        widgets  = {
            'Task_Assign_date' : forms.DateInput(attrs={'type':'date'}),
        }

        
    