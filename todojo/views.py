from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItem

def todoView(request):
    all = ToDoItem.objects.all()
    return render(request, 'todo.html',{'all_items': all})

def addItem(request):
    item = ToDoItem(text = request.POST['content'])
    item.save()
    return HttpResponseRedirect('/todo/')

def deleteItem(request, todo_id):
    item = ToDoItem.objects.get(id=todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')
