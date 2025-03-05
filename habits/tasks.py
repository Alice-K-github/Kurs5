from celery import shared_task
from habits.models import Habit
from users.services import send_telegram_message


@shared_task
def my_task(request, Habit_id):
    # Отправка уведомлений
    habit = Habit.objects.get(id=Habit_id)
    user = habit.owner
    message = f'Не забудь {habit.action} сегодня в {habit.in_time}!'
    if habit:
        if user.tg_chat_id:
            send_telegram_message(user.tg_chat_id, message)
