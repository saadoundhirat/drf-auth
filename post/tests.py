from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Post

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='saadoun', password='1234')
        testuser1.save()
        test_post = Post.objects.create(title='Test Post', body='Test Post Body', author=testuser1)
        test_post.save()
    
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author, 'saadoun')
        self.assertEqual(expected_title, 'Test Post')
        self.assertEqual(expected_body, 'Test Post Body')

# class APITest(APITestCase):
#     def test_list(self):
#         response = self.client.get(reverse('books_list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_detail(self):

#         test_user = get_user_model().objects.create_user(username='Noura',password='2551996')
#         test_user.save()

#         test_book = Book.objects.create(
#             author = test_user,
#             title = 'Cooking',
#             description = 'something about the book'
#         )
#         test_book.save()

#         response = self.client.get(reverse('books_detail', args=[1]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, {
#             'id':1,
#             'title': test_book.title,
#             'description': test_book.description,
#             'author': test_user.id,
#         })


#     def test_create(self):
#         test_user = get_user_model().objects.create_user(username='Noura',password='2551996')
#         test_user.save()


#         url = reverse('books_list')
#         data = {
#             "title":"Python!!!",
#             "description":"something about the book",
#             "author":test_user.id,
#         }

#         response = self.client.post(url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)
#         self.assertEqual(Book.objects.count(), 1)
#         self.assertEqual(Book.objects.get().title, data['title'])

#     def test_update(self):
#         test_user = get_user_model().objects.create_user(username='tester',password='pass')
#         test_user.save()

#         test_book = Book.objects.create(
#             author = test_user,
#             title = 'Title of Blog',
#             description = 'Words about the blog'
#         )

#         test_book.save()

#         url = reverse('books_detail',args=[test_book.id])
#         data = {
#             "title":"Python!!!",
#             "author":test_book.author.id,
#             "description":test_book.description,
#         }

#         response = self.client.put(url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_200_OK, url)

#         self.assertEqual(Book.objects.count(), test_book.id)
#         self.assertEqual(Book.objects.get().title, data['title'])


#     def test_delete(self):
#         """Test the api can delete a book."""

#         test_user = get_user_model().objects.create_user(username='tester',password='pass')
#         test_user.save()

#         test_book = Book.objects.create(
#             author = test_user,
#             title = 'Title of Blog',
#             description = 'Words about the blog'
#         )

#         test_book.save()

#         book = Book.objects.get()
#         url = reverse('books_detail', kwargs={'pk': book.id})
#         response = self.client.delete(url)
#         self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)