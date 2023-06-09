from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import CommentForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     template_name = 'books/book_detail.html'
#     model = Book
#     context_object_name = 'book'
@login_required
def book_detail_view(request, pk):
    # Getting book object
    book = get_object_or_404(Book, pk=pk)
    # Getting comments
    book_comments = book.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # We use commit = False, so we make an obj from the model but avoid  saving it on DB
            new_comment = comment_form.save(commit=False)
            # We know which book it is so =>
            new_comment.book = book
            # We also know that the user is accessible from request so =>
            new_comment.user = request.user
            # Now that every field of the form is full we can save and commit it on DB
            new_comment.save()
            # Return the empty form after redirection
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'comments': book_comments,
        'comment_form': comment_form
    })


class BookCreationView(LoginRequiredMixin, generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'description', 'price', 'cover']


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['title', 'author', 'description', 'cover']

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()  # We can get the object being used
        return obj.user == self.request.user  # To see if the owner is doing all the work?

