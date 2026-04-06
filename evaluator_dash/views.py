from django.shortcuts import render, get_object_or_404, redirect
from student_dash.models import Thesis
from .forms import EvaluationForm
from .models import Evaluation
from department.models import Instructor

# list of theses
def thesis_list(request):
    theses = Thesis.objects.all()
    return render(request,
                  'thesis_list.html',
                  {'theses': theses}
                  )

# thesis details
def thesis_detail(request, id):
    thesis = get_object_or_404(Thesis, id=id)
    evaluations = Evaluation.objects.filter(thesis=thesis)
    return render(request,
                  'thesis_detail.html',
                  {
                      'thesis': thesis,
                      'evaluations': evaluations
                  })
  
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
