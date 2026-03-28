from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Author, Publisher, Book
from .forms import AuthorForm, PublisherForm, BookForm

# Authors 
def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_authors')
    return render(request, 'library/form.html', {'form': form, 'title': 'Add Author'})

def list_authors(request):
    return render(request, 'library/list.html',
                  {'objects': Author.objects.all(), 'title': 'Authors'})

# Publishers
def add_publisher(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_publishers')
    return render(request, 'library/form.html', {'form': form, 'title': 'Add Publisher'})

def list_publishers(request):
    return render(request, 'library/list.html',
                  {'objects': Publisher.objects.all(), 'title': 'Publishers'})

# Books
def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'library/form.html', {'form': form, 'title': 'Add Book'})

def list_books(request):
    books = Book.objects.select_related('publisher').prefetch_related('authors').all()
    return render(request, 'library/books.html', {'books': books})