from django.urls import path
from .views import HomeView, AddStudent, ListStudents

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('student/add/', AddStudent.as_view(), name='student_form'),
    path('student/list/', ListStudents.as_view(), name = 'student_list'),
]