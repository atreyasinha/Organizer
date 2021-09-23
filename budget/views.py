from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BudgetSerializer
from .catSerializers import BudgetCategorySerializer

@login_required(login_url='loginUser')
# Create your views here.
def budget(request):
    budgets = Budget.objects.filter(user=request.user)

    form = BudgetForm()


    p = Budget.objects.filter(user=request.user).aggregate(Sum('projected'))['projected__sum']
    a = Budget.objects.filter(user=request.user).aggregate(Sum('actual'))['actual__sum']

    if a==None:
        diff = 0
    else:
        diff = p - a
        
    ans = "surplus"

    if (diff < 0):
        ans = "deficit"
        diff = diff * -1


    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user

            form.save()
        return redirect('budget')

    context = {'budgets': budgets, 'form': form, 'diff': diff, 'ans': ans}
    return render(request, 'budget/budget.html', context)

@login_required(login_url='loginUser')
def updateBudget(request, pk):
    budget = Budget.objects.get(id=pk)

    form = BudgetForm(instance=budget)

    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('budget')

    context = {'form': form}

    return render(request, 'budget/updateBudget.html', context)

@login_required(login_url='loginUser')
def deleteBudget(request, pk):
    budget = Budget.objects.get(id=pk)

    if request.method == 'POST':
        budget.delete()
        return redirect('budget')

    context = {'budget': budget}
    return render(request, 'budget/deleteBudget.html', context)

@api_view(['GET', 'POST'])
def apiBudget(request):
    budget = Budget.objects.filter(user=request.user)
    serializer = BudgetSerializer(budget, many=True)

    return Response(serializer.data)

@api_view(['GET', 'POST'])
def apiBudgetCategories(request):
    budget = Budget.objects.filter(user=request.user)
    serializer = BudgetCategorySerializer(budget, many=True)

    return Response(serializer.data)
