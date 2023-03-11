from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Section, Student, Teacher, Assignment, Submission
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import FileResponse
from .models import Section, Assignment, Submission, Student
from .forms import SubmissionForm,Assignment_create,Section_creation


def home(request):
    return render(request, 'home.html')


@login_required
def section_list(request):
    if request.user.is_superuser or request.user.is_staff:
        sections = Section.objects.all()
    else:
        sections = Section.objects.filter(student__user=request.user)

    return render(request, 'section_list.html', {'sections': sections})

@login_required
def Section_create(request):
    if request.method == 'POST':
        form = Section_creation(request.POST)
        if form.is_valid():
            assignment = form.save()
            return redirect('home')
    else:
        form = Section_creation()
    return render(request, 'section_creation.html', {'form': form})

@login_required
def section_detail(request, section_id):
    section = Section.objects.get(id=section_id)
    if request.user.is_superuser or request.user.is_staff:
        students = Student.objects.filter(section=section)
        assignments = Assignment.objects.filter(section=section).order_by("-pub_date")
    else:
        students = Student.objects.filter(user=request.user)
        assignments = Assignment.objects.filter(section=section)
    return render(request, 'section_detail.html', {'section': section, 'students': students, 'assignments': assignments})



@login_required
def assignment_creation(request):
    if request.method == 'POST':
        form = Assignment_create(request.POST ,request.FILES)
        if form.is_valid():
            assignment = form.save()
            return redirect('home')
    else:
        form = Assignment_create()
    return render(request, 'assignment_creation.html', {'form': form})

@login_required
def assignment_detail(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    students = Student.objects.all()
    submissions = Submission.objects.filter(assignment = assignment)

    if request.method == 'POST':
        submission = Submission.objects.create(
            student=Student.objects.get(user=request.user),
            assignment=assignment,
            file=request.FILES['file']
        )
        messages.success(request, f"Your submission for {assignment.title} was successful!")
        return redirect('assignment_detail', assignment_id=assignment.id)

    return render(request, 'assignment_detail.html', {'assignment': assignment, 'submissions': submissions, 'students':students})

@login_required
def submissionform(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST ,request.FILES)
        if form.is_valid():
            submission = form.save()
            messages.success(request, "Submission updated successfully.")
            return redirect('section_list')
    else:
        form = SubmissionForm()
    return render(request, 'submissionform.html', {'form': form})

@login_required
def gradesubmission(request, assignment_id, submission_id):
    if request.method == 'POST':
        grade = request.POST.get('grade',False)
        Submission.objects.filter(id=submission_id).update(grade=grade)
        return redirect('assignment_detail', assignment_id=assignment_id)
    return render(request,'grade.html')
        
