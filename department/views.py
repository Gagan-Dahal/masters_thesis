from django.shortcuts import render, redirect
from django.views import View
from .forms import StudentRegistrationForm, InstructorRegistrationForm, DepartmentRegistrationForm, CourseRegistrationForm
from django.contrib import messages
from .models import Student, Instructor, Department, Course


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    
class AddStudent(View):

    def get(self, request):
        empty_form = StudentRegistrationForm()
        return render(request, 'studentForm.html', {"form": empty_form})
    def post(self, request):
        print(request.POST)
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Added successfully")
            return redirect("home")
        messages.error(request, "Failed to add product")
        return render(request, "studentForm.html", {"form":form})
    
class ListStudents(View):

    def get(self, request):
        students = Student.objects.all()
        context_dict = {
            "students": students
        }
        return render(request, "studentList.html", context_dict)