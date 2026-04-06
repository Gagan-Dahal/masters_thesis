from django.db import models
from department.models import Instructor
from django.conf import settings


class Evaluation(models.Model):
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Revision', 'Need Revision'),
    ]
    thesis = models.ForeignKey('student_dash.Thesis', on_delete=models.CASCADE)
    evaluator = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    evaluation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.thesis.title
    
class ExternalEvaluator(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='external_evaluator')
    name = models.CharField(max_length=255)
    post = models.CharField(max_length=255) 
    qualification = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class EvaluationCommittee(models.Model):
    head_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='head')
    internal_member_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='internal_member')
    external_member_id = models.ForeignKey(ExternalEvaluator, on_delete=models.CASCADE, related_name='external_member')

class ThesisEvaluation(models.Model):
    thesis_id = models.ForeignKey('student_dash.Thesis', on_delete=models.CASCADE)
    committee_id = models.ForeignKey(EvaluationCommittee, on_delete=models.CASCADE)

