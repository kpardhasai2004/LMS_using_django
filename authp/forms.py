from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from lmsapp.models import Student, Section, Teacher


class StudentForm(UserCreationForm):
    email = forms.EmailField(required=True)
    section = forms.ModelChoiceField(queryset=Section.objects.all())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'section',]
    def save(self, commit=True):
        user = super(StudentForm, self).save(commit=False)
        user.is_student = True
        if commit:
            user.save()
            student = Student(user=user, section=self.cleaned_data['section'])
            student.save()
        return user


class TeacherForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField(initial=True, required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','is_staff',]
    def save(self, commit=True):
        user = super(TeacherForm, self).save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
            teacher = Teacher(user=user)
            teacher.save()
        return user
