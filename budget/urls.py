from django.urls import path
from . import views
import budget

urlpatterns = [
    path('budget/', views.budget, name="budget"),
    path('updateBudget/<str:pk>/', views.updateBudget, name="updateBudget"),
    path('deleteBudget/<str:pk>/', views.deleteBudget, name="deleteBudget"),

    path('api/v1/budget', views.apiBudget, name="apiBudget"),
    path('api/v1/budget-categories', views.apiBudgetCategories, name="apiBudgetCategories"),
]
