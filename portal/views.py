from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import RegistrationForm
from django.contrib import messages
from django.db.models import Sum


from task.models import *
from budget.models import *
from journal.models import *

# Create your views here.
def nav(request):
    return render(request, 'base.html')

def login(request):

    return render(request, 'portal/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = RegistrationForm()

        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save() 
                return redirect('loginUser')

        context = {'form': form}
        return render(request, 'portal/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('inputEmail')
            password = request.POST.get('inputPassword')
            user = authenticate(request, username=username, password=password)



            if user is not None:
                django_login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username/Password Incorrect. Please try again')

        context = {}

        return render(request, 'portal/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginUser')

@login_required(login_url='loginUser')
def dashboard(request):
    count = Journal.objects.filter(user=request.user).count()
    date = Journal.objects.filter(user=request.user).latest('created').created
    context = {'count': count, 'date': date}

    return render(request, 'portal/base.html', context)

@login_required(login_url='loginUser')
def dashboard(request):
    # journal
    count = Journal.objects.filter(user=request.user).count()

    if (Journal.objects.filter(user=request.user).count() == 0):
        date = "None"
    else:
        date = Journal.objects.filter(user=request.user).latest('created').created

    # budget
    if (Budget.objects.filter(user=request.user).count() == 0):
        p = 0
        a = 0
    else:
        p = Budget.objects.filter(user=request.user).aggregate(Sum('projected'))['projected__sum']
        a = Budget.objects.filter(user=request.user).aggregate(Sum('actual'))['actual__sum']

    # task
    t = Task.objects.filter(user=request.user).filter(completed=True).count()
    f = Task.objects.filter(user=request.user).filter(completed=False).count()

    context = {'count': count, 'date': date, 'p': p, 'a': a, 't': t, 'f': f}

    return render(request, 'portal/base.html', context)

@api_view(['GET'])
def apiOverview(request):   
    api_urls = {
        "tasks": "http://127.0.0.1:8000/api/v1/tasks",
        "task-categories": "http://127.0.0.1:8000/api/v1/task-categories",
        "budget": "http://127.0.0.1:8000/api/v1/budget",
        "budget-categories": "http://127.0.0.1:8000/api/v1/budget-categories",
        "journal": "http://127.0.0.1:8000/api/v1/journal",
    }

    return Response(api_urls)

@login_required(login_url='loginUser')
def about(request):
    return render(request, 'portal/about.html')
