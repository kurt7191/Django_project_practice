from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse



def index(request):
    todos = Todo.objects.all()
    content = {'todos' : todos}
    return render(request, 'my_to_do_app/index.html',content) ##html 을 view에서 보여줄때 사용하는 함수 render
    #request는 user나 session 정보를 담고 있으며, view로 화면을 보여줄 때 정보가 동시에 이동된다.

# Create your views here.

def createToDo(request):
    #return HttpResponse('create ToDo!!')
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    # return HttpResponse('create Todo=' + user_input_str)
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))


def boolTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))



