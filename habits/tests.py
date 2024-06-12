from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        """Создание Пользователя и Привычки"""
        self.user = User.objects.create(
            email='test@yandex.ru',
            password='test'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="22:00",
            action="Сон",
            duration=2,
            period='every_day'
        )
