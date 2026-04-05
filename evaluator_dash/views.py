from django.shortcuts import render, get_object_or_404, redirect
from student_dash.models import Thesis
from .forms import EvaluationForm
from .models import Evaluation

# list of theses
def thesis_list(request):
    theses = Thesis.objects.all()
    return render(request,
                  'evaluator_dash/thesis_list.html',
                  {'theses': theses}
                  )

# thesis details
def thesis_detail(request, id):
    thesis = get_object_or_404(Thesis, id=id)
    evaluations = Evaluation.objects.filter(thesis=thesis)
    return render(request,
                  'evaluator_dash/thesis_detail.html',
                  {
                      'thesis': thesis,
                      'evaluations': evaluations
                  })
  
# evaluate thesis
def evaluate_thesis(request, id):
    thesis = get_object_or_404(Thesis, id=id)
    form = EvaluationForm()
    if request.method == "POST":
        form = EvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.thesis = thesis
            # temporary evaluator (can replace with logged user later)
            evaluation.evaluator_id = 1
            evaluation.save()
            return redirect('thesis_detail', id=id)
    return render(request,
                  'evaluator_dash/evaluate.html',
                  {
                      'form': form,
                      'thesis': thesis
                  })
