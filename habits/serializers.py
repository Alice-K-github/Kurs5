from rest_framework import serializers
from habits.models import Habit
from habits.validators import RelatedHabitNotPleasantValidator, RewardValidator, NiceHabitValidator, TimeValidator, \
    PeriodValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            "owner", "place", "in_time", "action",
            "period", "reward", "take_time",
            "is_public")
        validators = [
            RelatedHabitNotPleasantValidator(field_1='related_habit'),
            RewardValidator(field_1='reward', field_2='related_habit'),
            NiceHabitValidator(field_1='is_nice', field_2='related_habit', field_3='reward'),
            TimeValidator(field='take_time'),
            PeriodValidator(field='period')
        ]
