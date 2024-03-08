from django import forms 
from category.models import TaskCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        exclude=['task']