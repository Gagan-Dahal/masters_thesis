from django.urls import path
from .views import HomeView, AddStudent, ListStudents,AddInstructor, ListInstructors, AddDepartment, ListDepartments, AddCourse, ListCourse, UserLogin, logout_view

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('student/add/', AddStudent.as_view(), name='student_form'),
    path('student/list/', ListStudents.as_view(), name = 'student_list'),
    path('department/add/', AddDepartment.as_view(), name='department_form'),
    path('department/list/', ListDepartments.as_view(), name = 'department_list'),
    path('course/add/', AddCourse.as_view(), name='course_form'),
    path('course/list/', ListCourse.as_view(), name = 'course_list'),
    path('instructor/add/', AddInstructor.as_view(), name='instructor_form'),
    path('instructor/list/', ListInstructors.as_view(), name = 'instructor_list'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]