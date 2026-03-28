from django.shortcuts import render

def home(request):
    context = {}

    if request.method == "POST":
        if 'display' in request.POST:
            name = request.POST.get('name')
            message = request.POST.get('message')

            bold = request.POST.get('bold')
            italic = request.POST.get('italic')
            underline = request.POST.get('underline')
            color = request.POST.get('color')

            full_message = f"{name} : {message}"

            style = ""

            if bold:
                style += "font-weight:bold;"
            if italic:
                style += "font-style:italic;"
            if underline:
                style += "text-decoration:underline;"
            if color:
                style += f"color:{color};"

            context = {
                'full_message': full_message,
                'style': style
            }

        elif 'clear' in request.POST:
            context = {}

        elif 'exit' in request.POST:
            return render(request, 'exit.html')

    return render(request, 'home.html', context)
