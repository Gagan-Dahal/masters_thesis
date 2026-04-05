from django import forms
from .models import Evaluation

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = [
            'comment',
            'status'
        ]
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your evaluation comment here...'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }
