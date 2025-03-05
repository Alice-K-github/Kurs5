from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated
from habits.models import Habit
from habits.paginators import HabitPagination
from habits.serializers import HabitSerializer


def home(request):
    return render(request, 'habits/home.html')


class Is_Owner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class HabitMyListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [Is_Owner]
    pagination_class = HabitPagination

    def get(self, request):
        user = self.request.user
        queryset = Habit.objects.all().filter(owner=user)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class HabitAllListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().filter(is_public='True')
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get(self, request):
        queryset = Habit.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [Is_Owner]


class HabitCreateAPIViewAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [Is_Owner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [Is_Owner]
