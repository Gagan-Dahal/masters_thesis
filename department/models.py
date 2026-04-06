from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=255)
    batch = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2200)
        ]
    )

    def __str__(self):
        return self.name
    
class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    post_choices = [
        ('PROFESSOR', 'Professor'),
        ('ASSOCIATE PROFESSOR', 'Associate Professor'),
        ('ASSISTANT PROFESSOR', 'Assistant Professor'),
        ('INSTRUCTOR', 'Instructor')
    ]
    post = models.CharField(max_length = 19, choices=post_choices)
    qualification = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=14)
    email = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique = True)
    head_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='head_department')
    deputy1_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='deputy1_department')
    deputy2_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='deputy2_department')
    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    credit = models.DecimalField(max_digits=5, decimal_places=2)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
