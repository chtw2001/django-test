from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Todo

def DeleteTodo(request, pk):
    delete_todo = get_object_or_404(Todo, pk=pk)
    delete_todo.delete()
    return redirect('/todo/')

def CompletedTodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.complete = True
    todo.save()
    return redirect('/todo/')

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['todo', 'description', 'important']

    template_name = 'todo_app/todo_update_form.html'


class TodoCreate(LoginRequiredMixin, CreateView): # LoginRequiredMixin을 사용하였기 때문에
    model = Todo                                  # 로그인이 필요함. 하지만 로그인되지 않았다면
    fields = ['todo', 'description', 'important'] # login_url로 이동하도록 함. 기본 설정은 다르게
    login_url = '/accounts/signin/'  # Custom login URL # 되어있어서 직접 지정해주어야 함


def Todos(request):
    todos = Todo.objects.all().order_by('pk')

    return render(
        request, 
        'todo_app/todos.html', 
        {'todos':todos},
        
        )

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo_app/index.html', {'todos':todos})