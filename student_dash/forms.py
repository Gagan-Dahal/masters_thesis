from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']

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
