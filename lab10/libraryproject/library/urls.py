from django.urls import path
from . import views

urlpatterns = [
    path('authors/add/',     views.add_author,      name='add_author'),
    path('authors/',         views.list_authors,    name='list_authors'),
    path('publishers/add/',  views.add_publisher,   name='add_publisher'),
    path('publishers/',      views.list_publishers, name='list_publishers'),
    path('books/add/',       views.add_book,        name='add_book'),
    path('books/',           views.list_books,      name='list_books'),
]