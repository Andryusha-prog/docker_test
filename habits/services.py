import datetime
import json

from django.utils import timezone
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from habits.models import Habits
from users.models import User


def create_periodic_task_for_tg(email, habit: Habits):
    chat_id = User.objects.get(email=email).tg_chat_id
    message = f"я буду {habit.action} в {habit.time} в {habit.place}"
    data_time = datetime.datetime.combine(timezone.now(), habit.time)

    PeriodicTask.objects.create(
        name=f"{habit.action}",
        task="habits.tasks.send_tg_message",
        interval=IntervalSchedule.objects.create(
            every=habit.periodic, period=IntervalSchedule.HOURS
        ),
        args=json.dumps([chat_id, message]),
        start_time=data_time,
    )
