from django.shortcuts import render, redirect
from .forms import StudentForm

def first_page(request):
    form = StudentForm()
    return render(request, 'sessionapp/firstPage.html', {'form': form})

def second_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subject'] = form.cleaned_data['subject']
            return redirect('second_page')

    name = request.session.get('name', '')
    roll = request.session.get('roll', '')
    subject = request.session.get('subject', '')
    return render(request, 'sessionapp/secondPage.html', {
        'name': name, 'roll': roll, 'subject': subject
    })