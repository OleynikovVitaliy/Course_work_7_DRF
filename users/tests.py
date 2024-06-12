from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        """ Создание Пользователя """
        self.user = User.objects.create(
            email='Oleinikov.Vitalik@yandex.ru',
            telegram_id=1461138162,
            password='12345'
        )

    def test_user_register(self):
        """ Создание Пользователя """
        data = {"email": "test@yandex.ru", "telegram_id": 12345, "password": "test12345"}
        response = self.client.post(reverse('users:register'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_detail(self):
        """ Вывод информации о пользователе"""
        response = self.client.get(reverse('users:user_detail', kwargs={'pk': self.user.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        """ Удаление Пользователя """
        response = self.client.delete(reverse('users:user_delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(id=self.user.pk).count(), 0)
