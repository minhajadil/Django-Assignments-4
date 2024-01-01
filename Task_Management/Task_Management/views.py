from django.shortcuts import render 
from task.models import TaskModel

def home(request):
    db = TaskModel.objects.all()
    return render(request,'home.html',{'db':db})