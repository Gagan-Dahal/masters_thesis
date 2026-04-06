from django.contrib import admin
from .models import Evaluation, ExternalEvaluator, EvaluationCommittee, ThesisEvaluation

admin.site.register(Evaluation)
admin.site.register(ExternalEvaluator)
admin.site.register(EvaluationCommittee)
admin.site.register(ThesisEvaluation)
