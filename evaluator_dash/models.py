from django.db import models
from department.models import Instructor
from student_dash.models import Thesis

class Evaluation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Revision', 'Need Revision'),
        ('Rejected', 'Rejected')
    ]
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    evaluator = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    evaluation_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.thesis.title
