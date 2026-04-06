from django.db import models
from django.conf import settings

class Thesis(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='student_thesis')
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='supervisor_thesis')
    evaluation_committee_id = models.ForeignKey('evaluator_dash.EvaluationCommittee', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    research_area = models.CharField(max_length=255)
    submission_date = models.DateField(auto_now_add=True)

class Document(models.Model):
    thesis = models.ForeignKey(Thesis,on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='docs/')
    DOC_TYPE = [
        ('REPORT', 'Report'),
        ('PROPOSAL', 'Proposal'),
    ]
    doc_type = models.CharField(
        max_length=20,
        choices=DOC_TYPE,
        default='REPORT'
    )
