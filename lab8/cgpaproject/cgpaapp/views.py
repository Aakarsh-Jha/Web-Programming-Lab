from django.shortcuts import render, redirect

def page1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        marks = request.POST.get('marks')

        # Store in session
        request.session['name'] = name
        request.session['marks'] = marks

        return redirect('page2')

    return render(request, 'cgpaapp/page1.html')


def page2(request):
    name = request.session.get('name')
    marks = request.session.get('marks')

    cgpa = None

    if name and marks:
        cgpa = float(marks) / 50

    return render(request, 'cgpaapp/page2.html', {
        'name': name,
        'cgpa': cgpa
    })