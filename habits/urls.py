from django.contrib import admin
from django.urls import path
from habits.models import Habit
from habits.serializers import HabitSerializer
from habits.views import home, HabitRetrieveAPIView, HabitCreateAPIViewAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitMyListAPIView, HabitAllListAPIView

app_name = 'habits'


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home),
    path('habit/My/', HabitMyListAPIView.as_view(
        queryset=Habit.objects.all(),
        serializer_class=HabitSerializer),
        name='habit_list_my'),
    path('habit/all/', HabitAllListAPIView.as_view(
        queryset=Habit.objects.all(),
        serializer_class=HabitSerializer),
        name='habit_list_all'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(
        queryset=Habit.objects.all(),
        serializer_class=HabitSerializer),
        name='habit_Retrieve'),
    path('habit/new/', HabitCreateAPIViewAPIView.as_view(
        queryset=Habit.objects.all(),
        serializer_class=HabitSerializer),
        name='habit_Create'),
    path('habit/<int:pk>/update/', HabitUpdateAPIView.as_view(
        queryset=Habit.objects.all(),
        serializer_class=HabitSerializer),
        name='habit_Update'),
    path('habit/<int:pk>/delete/', HabitDestroyAPIView.as_view(
        queryset=Habit.objects.all(),
        serializer_class=HabitSerializer),
        name='habit_Destroy'),
]
