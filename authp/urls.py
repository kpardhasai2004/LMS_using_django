from django.urls import path
from . import views as authp_views
from lmsapp import views as lmsapp_views
from lmsapp.views import (
    section_list, section_detail, assignment_detail, gradesubmission,home,
    assignment_creation,submissionform,Section_create,
)
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',home,name='home'),
    path('register_teacher/',authp_views.register_teacher,name='register_teacher'),
    path('register_student/',authp_views.register_student,name='register_student'),
    path('profile/',authp_views.profile, name='profile'),
    path('accounts/profile/',home, name='afterlogin'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),


    path('section_list/', section_list, name='section_list'),
    path('section_list/<int:section_id>/', section_detail, name='section_detail'),
    path('section_list/creation/', Section_create, name='section_create'),
    path('assignment/<int:assignment_id>/', assignment_detail, name='assignment_detail'),
    path('assignment/create/', assignment_creation,name='assignment_creation'),
    path('assignment/<int:submission_id>/submission/<int:assignment_id>/', gradesubmission, name='gradesubmission'),
    path('submission/create/', submissionform,name='submissionform'),
    ]