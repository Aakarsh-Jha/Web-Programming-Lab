from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Human

def index(request):
    
    if request.method == 'POST' and 'add' in request.POST:
        Human.objects.create(
            first_name = request.POST['first_name'],
            last_name  = request.POST['last_name'],
            phone      = request.POST['phone'],
            address    = request.POST['address'],
            city       = request.POST['city'],
        )
        return redirect('index')

    
    if request.method == 'POST' and 'update' in request.POST:
        h = Human.objects.get(id=request.POST['human_id'])
        h.first_name = request.POST['first_name']
        h.last_name  = request.POST['last_name']
        h.phone      = request.POST['phone']
        h.address    = request.POST['address']
        h.city       = request.POST['city']
        h.save()
        return redirect('index')

    
    if request.method == 'POST' and 'delete' in request.POST:
        Human.objects.filter(id=request.POST['human_id']).delete()
        return redirect('index')

    humans = Human.objects.all()
    return render(request, 'human/index.html', {'humans': humans})


def get_human(request, pk):
    
    h = Human.objects.get(id=pk)
    return JsonResponse({
        'id':         h.id,
        'first_name': h.first_name,
        'last_name':  h.last_name,
        'phone':      h.phone,
        'address':    h.address,
        'city':       h.city,
    })