from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="loginUser"),
    path('logout/', views.logoutUser, name="logoutUser"),
    path('register/', views.register, name="register"),
    # path('', views.dashboard, name="dashboard"),
    # path('about/', views.about, name="about"),

    # path('api/v1/', views.apiOverview, name="apiOverview"),

]
