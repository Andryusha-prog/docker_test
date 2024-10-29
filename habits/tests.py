from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


# Create your tests here.
class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test_user@test.ru")
        self.habit = Habits.objects.create(
            action="test action",
            place="home",
            periodic=24,
            time="12:00",
            user=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_create(self):
        url = reverse("habits:create")
        data = {"action": "test action 2", "time": "00:00", "periodic": 24}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_update(self):
        url = reverse("habits:update", args=(self.habit.pk,))
        data = {"place": "street"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_list(self):
        url = reverse("habits:list")
        response = self.client.get(url)
        data = response.json()

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 6,
                    "place": self.habit.place,
                    "time": "12:00:00",
                    "action": self.habit.action,
                    "is_enjoined": False,
                    "periodic": self.habit.periodic,
                    "award": None,
                    "time_action": None,
                    "is_public": False,
                    "user": self.user.pk,
                    "related_habit": None,
                }
            ],
        }
        self.assertEqual(data, result)

    def test_habit_delete(self):
        url = reverse("habits:delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
