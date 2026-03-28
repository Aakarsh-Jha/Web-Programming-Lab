from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from instapp.models import Institute

def institute_list(request):
    institutes = Institute.objects.all()
    return render(request, 'instapp/institute.html', {'institutes': institutes})