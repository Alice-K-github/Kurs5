from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from habits.models import Habit
from users.models import CustomUser


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email='admin@example.com',
            password="123123")
        self.habit = Habit.objects.create(
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse('habits:habit_Retrieve', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('owner'), self.habit.owner)

    def test_habit_create(self):
        # Есть вознаграждение
        url = reverse('school:habit_Create')
        data = {'action': 'выпить воды',
                'reward': 'поесть шоколад',
                }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse('habits:habit_Update', args=(self.habit.pk,))
        data = {'action': 'выпить воды'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('action'), 'выпить воды')

    def test_habit_delete(self):
        url = reverse('habits:habit_Destroy', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse('habits:habit_list_all')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {'count': 1, 'next': None, 'previous': None, 'results':
                [{'id': self.habit.pk,
                  'place': None,
                  'in_time': None,
                  'action': 'выпить воды', 'period': 1,
                  'reward': None, 'take_time': 50,
                  'is_public': True, 'is_nice': False,
                  'related_habit': None,
                  'owner': self.habit.owner.id}]}
        )
