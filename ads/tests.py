from django.urls.base import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User
from .models import Ad, Comment


class AdViewSetsTestCase(APITestCase):

    def setUp(self) -> None:
        # Создание тестового пользователя
        self.user = User.objects.create(
            email='test@mail.ru',
            password='Test123test'
        )
        # Аутентификация пользователя
        self.client.force_authenticate(
            user=self.user
        )
        # Создание тестовое объявление
        self.ad = Ad.objects.create(
            title='advertisement',
            author=self.user,
            price=100,
            description='description'
        )

    def test_ad_create(self):
        """
        Тест создания объявления
        """
        url = reverse('ads:ad-create')
        data = {
            'title': 'test_title',
            'author': self.user.pk,
            'price': 10,
            'description': 'test_description',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        ad = Ad.objects.get(title='test_title')
        author = self.user
        self.assertEqual(author, ad.author)
        self.assertEqual(Ad.objects.all().count(), 2)

    def test_retrieve_ad(self):
        """
        Тест просмотра одного объявления
        """
        url = reverse('ads:ad-detail', args=[self.ad.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('price'), self.ad.price)

    def test_update_ad(self):
        """
        Тест редактирования объявления
        """
        url = reverse('ads:ad-update', args=[self.ad.pk])
        data = {
            'title': 'test_title_update',
            'description': 'test_description_update'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ad.refresh_from_db()
        self.assertEqual(self.ad.title, 'test_title_update')
        self.assertEqual(self.ad.description, 'test_description_update')

    def test_delete_ad(self):
        """
        Тест удаления объявления
        """
        url = reverse('ads:ad-delete', args=[self.ad.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ad.objects.all().count(), 0)
        self.assertFalse(Ad.objects.filter(id=self.ad.id).exists())


class CommentViewSetsTestCase(APITestCase):

    def setUp(self) -> None:
        # Создание тестового пользователя
        self.user = User.objects.create(
            email='test@mail.ru',
            password='Test123test'
        )
        # Аутентификация пользователя
        self.client.force_authenticate(
            user=self.user
        )
        # Создание тестовое объявление
        self.ad = Ad.objects.create(
            title='advertisement',
            author=self.user,
            price=100,
            description='description'
        )
        # Создание тестовое комментария
        self.comment = Comment.objects.create(
            text="test_comment",
            author=self.user,
            ad=self.ad
        )

    def test_comment_create(self):
        """
        Тест создания отзыва
        """
        data = {
            'text': 'test_comment_new',
            'author': self.user.pk,
            'ad': self.ad.pk
        }
        url = f'/ads/{self.ad.pk}/comments/'
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        comment = Comment.objects.get(text='test_comment_new')
        author = self.user
        self.assertEqual(author, comment.author)
        self.assertEqual(Comment.objects.all().count(), 2)

    def test_retrieve_comment(self):
        """
        Тест просмотра отзыва
        """
        url = f'/ads/{self.ad.pk}/comments/{self.comment.pk}/'
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('text'), self.comment.text)

    def test_update_comment(self):
        """
        Тест редактирования отзыва
        """
        url = f'/ads/{self.ad.pk}/comments/{self.comment.pk}/'
        data = {
            'text': 'test_comment_update '
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.text, 'test_comment_update')

    def test_delete_comment(self):
        """
        Тест удаления отзыва
        """
        url = f'/ads/{self.ad.pk}/comments/{self.comment.pk}/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.all().count(), 0)
        self.assertFalse(Comment.objects.filter(id=self.ad.id).exists())
