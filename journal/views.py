from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JournalSerializer

# Create your views here.
@login_required(login_url='loginUser')
# Create your views here.
def journal(request):
    journals = Journal.objects.filter(user=request.user)

    context = {'journals': journals}
    return render(request, 'journal/journal.html', context)

@login_required(login_url='loginUser')
def addJournal(request):
    form = JournalForm()

    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user

            form.save()
        return redirect('journal')

    context = {'form': form}
    return render(request, 'journal/addJournal.html', context)

@login_required(login_url='loginUser')
def updateJournal(request, pk):
    journal = Journal.objects.get(id=pk)

    form = JournalForm(instance=journal)

    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal)
        if form.is_valid():
            form.save()
            return redirect('journal')

    context = {'form': form}

    return render(request, 'journal/updateJournal.html', context)

@login_required(login_url='loginUser')
def deleteJournal(request, pk):
    journal = Journal.objects.get(id=pk)

    if request.method == 'POST':
        journal.delete()
        return redirect('journal')

    context = {'journal': journal}

    return render(request, 'journal/deleteJournal.html', context)

@login_required(login_url='loginUser')
def showJournal(request, pk):
    journal = Journal.objects.get(id=pk)

    context = {'journal': journal}

    return render(request, 'journal/showJournal.html', context)

@api_view(['GET', 'POST'])
def apiJournal(request):
    journal = Journal.objects.filter(user=request.user)
    serializer = JournalSerializer(journal, many=True)

    return Response(serializer.data)