from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "place",
        "in_time",
        "action",
        "period",
        "reward",
        "take_time",
        "is_public",
        "is_nice",
        "related_habit",
    )
