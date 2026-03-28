from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from directory.models import Category, Page, CategoryForm, PageForm

def index(request):
    categories = Category.objects.all()
    pages = Page.objects.all()
    return render(request, 'directory/index.html', {'categories': categories, 'pages': pages})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CategoryForm()
    return render(request, 'directory/add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PageForm()
    return render(request, 'directory/add_page.html', {'form': form})