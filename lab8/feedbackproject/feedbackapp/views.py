from django.shortcuts import render

def feedback(request):
    message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')

        if gender == "Male":
            title = "Mr."
        else:
            title = "Ms."

        message = f"Thank You {title} {name} for your feedback."

    return render(request, 'feedbackapp/feedback.html', {'message': message})