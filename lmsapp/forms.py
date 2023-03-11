from django import forms
from django.contrib.auth.models import User
from .models import *


class SubmissionForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    assignment = forms.ModelChoiceField(queryset=Assignment.objects.all())
    class Meta:
        model = Submission
        fields = ['student','assignment','file',]

class Assignment_create(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    section = forms.ModelChoiceField(queryset=Section.objects.all())
    class Meta:
        model = Assignment
        fields = ['title','description','section','teacher','file',]

class Section_creation(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    class Meta:
        model = Section
        fields = ['section_name','teacher']


