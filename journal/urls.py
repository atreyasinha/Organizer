from django.urls import path
from . import views
import journal

urlpatterns = [
    path('journal/', views.journal, name="journal"),
    path('addJournal/', views.addJournal, name="addJournal"),
    path('updateJournal/<str:pk>/', views.updateJournal, name="updateJournal"),
    path('deleteJournal/<str:pk>/', views.deleteJournal, name="deleteJournal"),
    path('showJournal/<str:pk>/', views.showJournal, name="showJournal"),

    path('api/v1/journal', views.apiJournal, name="apiJournal"),

]
