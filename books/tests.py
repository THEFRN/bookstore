from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Book


class TestBooks(TestCase):
    user_name = 'username'

    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(age=28, username='username')
        cls.book1 = Book.objects.create(
            title='title',
            author=user,
            price=19.20,
            description='description'
        )

    def test_url_books_list(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_url_books_list_by_name(self):
        response = self.client.get(reverse('book_list'))

    def test_books_list_template(self):
        response = self.client.get(reverse('book_list'))
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_books_list_body_contains(self):
        response = self.client.get(reverse('book_list'))
        self.assertContains(response, 'Books List')

    def test_books_detail_url(self):
        response = self.client.get(f'/books/{self.book1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_books_detail_does_not_exist(self):
        response = self.client.get(f'/books/100000/')
        self.assertEqual(response.status_code, 404)

    def test_books_detail_existence(self):
        response = self.client.get(reverse('book_detail', args=[self.book1.id]))
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book1.description)

    def test_book_detail_url_by_name(self):
        response = self.client.get(reverse('book_detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_detail_containment(self):
        response = self.client.get(reverse('book_detail', args=[self.book1.id]))
        self.assertContains(response, self.book1.title)

    def test_book_creation_url(self):
        response = self.client.get('/books/create/')
        self.assertEqual(response.status_code, 200)

    def test_book_creation_url_by_name(self):
        response = self.client.get(reverse('book_creation'))
        self.assertEqual(response.status_code, 200)

    def test_book_creation_form(self):
        self.assertEqual(self.book1.title, 'title')
        self.assertEqual(self.book1.price, 19.20)
        self.assertEqual(self.book1.description, 'description')

    def test_book_creation_containment(self):
        response = self.client.get(reverse('book_creation'))
        self.assertContains(response, 'Add A Book')

    def test_book_creation_template(self):
        response = self.client.get(reverse('book_creation'))
        self.assertTemplateUsed('books/book_create.html')

    def test_book_edit_url(self):
        response = self.client.get(f'/books/{self.book1.id}/edit/')
        self.assertEqual(response.status_code, 200)

    def test_book_edit_url_by_name(self):
        response = self.client.get(reverse('book_update', args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_edit_template(self):
        response = self.client.get(reverse('book_update', args=[self.book1.id]))
        self.assertTemplateUsed('books/book_update.html')

    def test_book_edit_containment(self):
        response = self.client.get(reverse('book_update', args=[self.book1.id]))
        self.assertContains(response, 'Edit A Book')

    def test_book_delete_by_url(self):
        response = self.client.get(f'/books/{self.book1.id}/delete/')
        self.assertEqual(response.status_code, 200)

    def test_book_delete_url_by_name(self):
        response = self.client.get(reverse('book_delete', args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_delete_template(self):
        response = self.client.get(reverse('book_delete', args=[self.book1.id]))
        self.assertTemplateUsed('books/book_delete.html')

    def test_book_delete_containment(self):
        response = self.client.get(reverse('book_delete', args=[self.book1.id]))
        self.assertContains(response, 'Delete A Book')
