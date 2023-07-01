from django.urls import path
from . import views

urlpatterns = [
    path('', views.Todos, name="todo_list"),
    path('create_todo/', views.TodoCreate.as_view()),
    path('update_todo/<int:pk>/', views.TodoUpdate.as_view()),
    path('delete_todo/<int:pk>/', views.DeleteTodo),
    path('completed_todo/<int:pk>/', views.CompletedTodo),

    path('index/', views.index)

]