from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from evaluator_dash.models import Evaluation
from .forms import DocumentForm, ThesisForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages

@login_required
def addrevised(request):
    if request.method == 'POST':
        thesis = request.user.student_thesis.first()
        doc_form = DocumentForm(request.POST, request.FILES)
        if  doc_form.is_valid():
            doc = doc_form.save(commit=False)
            doc.thesis = thesis
            doc.doc_type="Report"
            doc.save()
            return redirect('sdashboard')
    else:
        doc_form = DocumentForm()
    return render(request, 'addrevised.html', {
        'doc_form': doc_form
    })    

@login_required
def upload(request):
    if request.method == 'POST':
        thesis_form = ThesisForm(request.POST)
        doc_form1 = DocumentForm(request.POST, request.FILES)
        doc_form2 = DocumentForm(request.POST, request.FILES)
        if thesis_form.is_valid() and doc_form1.is_valid() and doc_form2.is_valid():
            thesis = thesis_form.save(commit=False)
            thesis.user = request.user
            thesis.save()

            doc = doc_form1.save(commit=False)
            doc.thesis = thesis
            doc.doc_type="Report"
            doc.save()

            doc = doc_form2.save(commit=False)
            doc.thesis = thesis
            doc.doc_type="Proposal"
            doc.save()
            return redirect('sdashboard')
    else:
        thesis_form = ThesisForm()
        doc_form1 = DocumentForm()
        doc_form2 = DocumentForm()
    return render(request, 'upload.html', {
        'thesis_form': thesis_form,
        'doc_form1': doc_form1,
        'doc_form2': doc_form2
    })    

class StdDashboardView(LoginRequiredMixin, UserPassesTestMixin,View):
    def test_func(self):
        return hasattr(self.request.user, 'student')
    def handle_no_permission(self):
        messages.error(self.request, "You are not authorized to access this page.")
        return redirect('home')
    def get(self,request):
        user = request.user
        thesis = user.student_thesis.first()
        document = thesis.document_set.all() if thesis is not None else None
        evaluation = Evaluation.objects.filter(thesis=thesis).first()
        context = {
            'thesis': thesis,
            'doc':document,
            'eval':evaluation
        }
        return render(request,'dashboard.html',context)
