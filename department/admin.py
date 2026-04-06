from django.contrib import admin
from .models import Student, Instructor, Department, Course, Enrollment

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Enrollment)
