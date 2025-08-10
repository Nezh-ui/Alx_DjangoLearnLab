from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.other_user = User.objects.create_user(username='otheruser', password='pass456')

        self.book1 = Book.objects.create(title='Django Unleashed', author='Andrew Pinkham', publication_year=2015)
        self.book2 = Book.objects.create(title='Two Scoops of Django', author='Daniel Roy Greenfeld', publication_year=2019)
        self.book3 = Book.objects.create(title='Effective Python', author='Brett Slatkin', publication_year=2020)

        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', args=[self.book1.id])
        self.update_url = reverse('book-update', args=[self.book1.id])
        self.delete_url = reverse('book-delete', args=[self.book1.id])
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)

    def test_create_book(self):
        self.client.login(username='testuser', password='pass123')
        response = self.client.post(self.create_url, {    # handle book creation
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2021
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_update_book(self):
        self.client.login(username='testuser', password='pass123')
        response = self.client.put(self.update_url, {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publication_year': 2022
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        self.client.login(username='testuser', password='pass123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)
    
    def test_filter_books(self):
        response = self.client.get(self.list_url, {'publication_year': 2019})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['title'], 'Two Scoops of Django')
    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
        self.assertIn('Django Unleashed', [book['title'] for book in response.json()])
        self.assertIn('Two Scoops of Django', [book['title'] for book in response.json()])
    def test_search_books_no_results(self):
        response = self.client.get(self.list_url, {'search': 'Nonexistent Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 0)
