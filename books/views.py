from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    model = Book
    context_object_name = 'book'