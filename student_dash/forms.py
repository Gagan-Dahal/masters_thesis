from django.contrib.auth import get_user_model
from django import forms
from .models import Thesis, Document

class ThesisForm(forms.ModelForm):
    class Meta:
        model = Thesis
        fields = ['title', 'research_area', 'supervisor']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']
