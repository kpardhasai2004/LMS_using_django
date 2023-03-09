from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import StudentForm,TeacherForm
from django.contrib.auth.decorators import login_required
from .models import Use
from django.contrib.auth import authenticate, login
from lmsapp.views import *
# Create your views here.

@login_required()
def register_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = TeacherForm()

    return render(request, 'register_teacher.html', {'form': form})

@login_required()
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = StudentForm()

    return render(request, 'register_student.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'profile.html')