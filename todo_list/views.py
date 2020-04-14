from django.shortcuts import render,redirect
from .models import Todo
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    todo_items=Todo.objects.all().order_by("-added_date")
    return render(request,'index.html',{'todo_items':todo_items})

@csrf_exempt
def add_todo(request):
    currentdate=timezone.now()
    content=request.POST["content"]
    Todo.objects.create(added_date=currentdate , text=content)
    return redirect('/')

@csrf_exempt
def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')
