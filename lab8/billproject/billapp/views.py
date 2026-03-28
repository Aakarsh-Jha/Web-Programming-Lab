from django.shortcuts import render

# Sample Prices (you can modify)
PRICES = {
    'Mobile': 10000,
    'Laptop': 50000,
}

def page1(request):
    return render(request, 'billapp/page1.html')


def page2(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        items = request.POST.getlist('item')
        quantity = int(request.POST.get('quantity'))

        total = 0

        for item in items:
            total += PRICES[item] * quantity

        context = {
            'brand': brand,
            'items': items,
            'quantity': quantity,
            'total': total
        }

        return render(request, 'billapp/page2.html', context)