from django.urls import path
from. import views

urlpatterns=[
    path('',views.index, name='index'),
    path('createToDo/',views.createToDo, name='createTodo'),
    path('doneTodo/',views.deleteTodo, name = 'doneTodo'),
    path('boolTodo/', views.boolTodo, name = 'boolTodo')
    
]