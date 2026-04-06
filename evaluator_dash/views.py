from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from student_dash.models import Thesis
from .forms import EvaluationForm
from .models import Evaluation
from department.models import Instructor
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class InstDashboardView(LoginRequiredMixin, UserPassesTestMixin,View):
    def test_func(self):
        return hasattr(self.request.user, 'instructor')
    def handle_no_permission(self):
        messages.error(self.request, "You are not authorized to access this page.")
        return redirect('home')
    def get(self,request):
        theses = Thesis.objects.all()
        return render(request,
                  'thesis_list.html',
                  {'theses': theses}
                  )



@login_required
def thesis_detail(request, id):
    thesis = get_object_or_404(Thesis, id=id)
    evaluations = Evaluation.objects.filter(thesis=thesis)
    documents = thesis.document_set.all()
    return render(request,
                  'thesis_detail.html',
                  {
                      'thesis': thesis,
                      'evaluations': evaluations,
                      'documents': documents,
                  })
  
@login_required  
def evaluate_thesis(request, id):

    thesis = get_object_or_404(Thesis, id=id)

    form = EvaluationForm()

    if request.method == "POST":

        form = EvaluationForm(request.POST)

        if form.is_valid():

            evaluation = form.save(commit=False)

            evaluation.thesis = thesis

            # auto select first instructor
            evaluator = Instructor.objects.first()
            print(evaluator)
            evaluation.evaluator = evaluator

            evaluation.save()

            return redirect('thesis_detail', id=id)

    return render(request,
                  'evaluate.html',
                  {
                      'form': form,
                      'thesis': thesis
                  })
