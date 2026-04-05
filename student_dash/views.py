from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm, RegisterForm, ThesisForm, User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

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

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) 
            return redirect('sdashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    thesis = user.student_thesis.first()
    context = {
        'thesis': thesis
    }
    return render(request,'dashboard.html',context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()   # creates user
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
