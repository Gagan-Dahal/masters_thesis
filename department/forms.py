from django.forms import ModelForm
from django import forms
from .models import Student, Instructor, Course, Department
from django.contrib.auth.models import User


class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('id', 'user',)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email    
    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            user = User.objects.create_user(
                username=self.cleaned_data['email'],
                password=self.cleaned_data['phone'],
            )
            student.user = user

            student.save()
        return student


class InstructorRegistrationForm(ModelForm):
    class Meta:
        model = Instructor
        exclude = ('id', 'user',)

    def save(self, commit=True):
        instructor = super().save(commit=False)
        if commit:
            user = User.objects.create_user(
                username=self.cleaned_data['email'],
                password=self.cleaned_data['contact_number'],
            )
            instructor.user = user

            instructor.save()
        return instructor

class DepartmentRegistrationForm(ModelForm):
    class Meta:
        model = Department
        exclude = ('id',)
        labels = {
            'name': 'Department Name',
            'head_id': 'Head of Department',
            'deputy1_id': 'Deputy 1',
            'deputy2_id': 'Deputy 2',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['head_id'].empty_label = "Select Head"
        self.fields['deputy1_id'].empty_label = "Select Deputy 1"
        self.fields['deputy2_id'].empty_label = "Select Deputy 2"

class CourseRegistrationForm(ModelForm):
    class Meta:
        model = Course
        exclude = ('id',)