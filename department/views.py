from django.shortcuts import render, redirect
from django.views import View
from .forms import StudentRegistrationForm, InstructorRegistrationForm, DepartmentRegistrationForm, CourseRegistrationForm
from django.contrib import messages
from .models import Student, Instructor, Department, Course
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# Create your views here.
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home.html')
    
class AddStudent(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        empty_form = StudentRegistrationForm()
        return render(request, 'studentForm.html', {"form": empty_form})
    def post(self, request):
        print(request.POST)
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Added Successfully")
            return redirect("home")
        messages.error(request, "Failed to add product")
        return render(request, "studentForm.html", {"form":form})
    
class ListStudents(LoginRequiredMixin, View):

    def get(self, request):
        students = Student.objects.all()
        context_dict = {
            "students": students
        }
        return render(request, "studentList.html", context_dict)
    
class AddInstructor(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        empty_form = InstructorRegistrationForm()
        return render(request, 'instructorForm.html', {"form": empty_form})
    def post(self, request):
        print(request.POST)
        form = InstructorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Instructor Added successfully")
            return redirect("home")
        messages.error(request, "Failed to add instructor")
        return render(request, "instructorForm.html", {"form":form})
    
class ListInstructors(LoginRequiredMixin, View):

    def get(self, request):
        instructors = Instructor.objects.all()
        context_dict = {
            "instructors": instructors
        }
        return render(request, "instructorList.html", context_dict)
    

class AddDepartment(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        empty_form = DepartmentRegistrationForm()
        return render(request, 'departmentForm.html', {"form": empty_form})
    def post(self, request):
        print(request.POST)
        form = DepartmentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department Added successfully")
            return redirect("home")
        messages.error(request, "Failed to add department")
        return render(request, "departmentForm.html", {"form":form})
    
class ListDepartments(LoginRequiredMixin, View):

    def get(self, request):
        departments = Department.objects.all()
        context_dict = {
            "departments": departments
        }
        return render(request, "departmentList.html", context_dict)

class AddCourse(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        empty_form = CourseRegistrationForm()
        return render(request, 'courseForm.html', {"form": empty_form})
    def post(self, request):
        print(request.POST)
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course Added successfully")
            return redirect("home")
        messages.error(request, "Failed to add course")
        return render(request, "courseForm.html", {"form":form})
    

class ListCourse(LoginRequiredMixin, View):

    def get(self, request):
        courses = Course.objects.all()
        context_dict = {
            "courses": courses
        }
        return render(request, "courseList.html", context_dict)
    


class UserLogin(View):
    def get(self, request):
        next_url = request.GET.get('next')
        return render(request, "login.html", {'next': next})
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            if next_url:
                return redirect(next_url)
            return redirect('home')
        
        messages.error(request, "Credentials Do Not Match")
        return render(request, "login.html", {'username': username, 'next': next_url})


def logout_view(request):
    logout(request)
    return redirect('login')