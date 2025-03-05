from django.db.models import CASCADE
from django.db import models
from users.models import CustomUser
from datetime import timedelta


class Habit(models.Model):
    # Курсы
    owner = models.ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        verbose_name="Пользователь",
        blank=True, null=True)
    place = models.CharField(
        verbose_name='Место для выполнения',
        blank=True, null=True)
    in_time = models.TimeField(
        verbose_name='Время выполнения',
        blank=True, null=True)
    action = models.CharField(
        verbose_name='Действие',
        blank=True, null=True)
    period = models.PositiveSmallIntegerField(default=1, verbose_name='Периодичность выполнения (раз в кол-во дней, default=1 раз в день)', blank=True, null=True)
    reward = models.CharField(verbose_name='Вознаграждение', blank=True, null=True)
    take_time = models.DurationField(default=timedelta(seconds=100), verbose_name='Время на выполнение', blank=True, null=True)
    is_public = models.BooleanField(verbose_name='Признак публикации', blank=True, null=True)
    is_nice = models.BooleanField(verbose_name='Признак приятной привычки', blank=True, null=True)
    related_habit = models.ForeignKey('self', on_delete=CASCADE, verbose_name='Связанная привычка', blank=True, null=True)

    def __str__(self):
        return f'{self.owner} {self.place} {self.in_time} {self.action} {self.period} {self.take_time} {self.is_public}'

    class Meta:
        verbose_name = 'наименование полезной привычки'
        verbose_name_plural = 'наименования полезных привычек'
