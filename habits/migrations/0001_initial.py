# Generated by Django 4.2.19 on 2025-03-05 21:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        blank=True, null=True, verbose_name="Место для выполнения"
                    ),
                ),
                (
                    "in_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="Время выполнения"
                    ),
                ),
                (
                    "action",
                    models.CharField(blank=True, null=True, verbose_name="Действие"),
                ),
                (
                    "period",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        default=1,
                        null=True,
                        verbose_name="Периодичность выполнения (раз в кол-во дней, default=1 раз в день)",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True, null=True, verbose_name="Вознаграждение"
                    ),
                ),
                (
                    "take_time",
                    models.DurationField(
                        blank=True,
                        default=datetime.timedelta(seconds=100),
                        null=True,
                        verbose_name="Время на выполнение",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Признак публикации"
                    ),
                ),
                (
                    "is_nice",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "наименование полезной привычки",
                "verbose_name_plural": "наименования полезных привычек",
            },
        ),
    ]
