from django.shortcuts import render, redirect
from .forms import CarForm

def car_form(request):
    form = CarForm()
    return render(request, 'carapp/form.html', {'form': form})

def car_result(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            manufacturer = form.cleaned_data['manufacturer']
            model = form.cleaned_data['model']
            return render(request, 'carapp/result.html', {'manufacturer': manufacturer, 'model': model})
    return redirect('car_form')