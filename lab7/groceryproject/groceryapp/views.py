from django.shortcuts import render
from .forms import GroceryForm

PRICES = {
    'Wheat': 40,
    'Jaggery': 60,
    'Dal': 80,
    'Rice': 50,
    'Sugar': 45,
    'Salt': 20,
}

def grocery_view(request):
    selected_items = []
    form = GroceryForm()

    if request.method == 'POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            chosen = form.cleaned_data['items']
            selected_items = [{'name': item, 'price': PRICES[item]} for item in chosen]

    return render(request, 'groceryapp/grocery.html', {
        'form': form,
        'selected_items': selected_items
    })