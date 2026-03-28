from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, 'students/index.html', {'form': form, 'students': students})