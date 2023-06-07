from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from .models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     template_name = 'books/book_detail.html'
#     model = Book
#     context_object_name = 'book'

def book_detail_view(request, pk):
    # Getting book object
    book = get_object_or_404(Book, pk=pk)
    # Getting comments
    book_comments = book.comments.all()
    return render(request, 'books/book_detail.html', {
        'book': book,
        'comments': book_comments,
    })


class BookCreationView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'description', 'price', 'cover']


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['title', 'author', 'description', 'cover']


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
