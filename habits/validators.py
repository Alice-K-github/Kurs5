from datetime import timedelta

from rest_framework.exceptions import ValidationError


class RelatedHabitNotPleasantValidator:

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, value):
        related_habit = dict(value).get(self.field_1)
        if not related_habit:
            return
        if not related_habit.is_nice:
            raise ValidationError("Связанная привычка должна быть приятной")


class RewardValidator:

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        reward = dict(value).get(self.field_1)
        related_habit = dict(value).get(self.field_2)
        if reward and related_habit:
            raise ValidationError("Нельзя одновременно заполнить вознаграждение и связанную привычку.")


class NiceHabitValidator:

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        is_nice = dict(value).get(self.field_1)
        related_habit = dict(value).get(self.field_2)
        reward = dict(value).get(self.field_3)
        if not is_nice:
            return
        if is_nice:
            if related_habit:
                raise ValidationError("У приятной привычки нет связанной привычки")
            if reward:
                raise ValidationError("У приятной привычки нет вознаграждения")
            else:
                return


class TimeValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = dict(value).get(self.field)
        if not time:
            return
        if time < timedelta(seconds=120):
            raise ValidationError("Время выполнения не может превышать 120 секунд")


class PeriodValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        period = dict(value).get(self.field)
        if not period:
            return
        if period > 7:
            raise ValidationError("Выполнять привычку можно не реже раза в неделю")
