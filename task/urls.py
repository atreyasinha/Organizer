from django.urls import path
from . import views
import task

urlpatterns = [
    path('todo/', views.todo, name="todo"),
    path('update/<str:pk>/', views.updateTask, name="update"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),


    path('api/v1/tasks', views.apiTasks, name="apiTasks"),
    path('api/v1/task-categories', views.apiTasksCategories, name="apiTasksCategories"),
]
