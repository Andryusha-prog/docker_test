from django.db import models

from config import settings


# Create your models here.
class Habits(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="пользователь",
        blank=True,
        null=True,
    )
    place = models.CharField(
        max_length=150,
        verbose_name="место выполнения привчки",
        blank=True,
        null=True,
        help_text="введите место выполнения привычки",
    )
    time = models.TimeField(
        verbose_name="время выполнения привычки",
        blank=True,
        null=True,
        help_text="введите время выполнения привычки",
    )
    action = models.CharField(
        max_length=200,
        verbose_name="привычка",
        help_text="Введите название привычки",
    )
    is_enjoined = models.BooleanField(
        verbose_name="признак приятной привычки",
        help_text="укажите признак приятной привычки",
        default=False,
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="связанная привычка",
    )
    periodic = models.PositiveIntegerField(
        verbose_name="периодичность выполения привычки",
        help_text="введите периодичность выполнения привычки в часах",
        blank=True,
        null=True,
    )
    award = models.CharField(
        max_length=200,
        verbose_name="вознаграждение",
        help_text="вознаграждение за выполнение привычки",
        blank=True,
        null=True,
    )
    time_action = models.PositiveIntegerField(
        verbose_name="длительность выполнения",
        blank=True,
        null=True,
        help_text="введите длительность выполнения",
    )
    is_public = models.BooleanField(
        verbose_name="признак публичности привычки",
        help_text="укажите признак публичности привычки",
        default=False,
    )

    class Meta:
        verbose_name = "Полезная привычка"
        verbose_name_plural = "Полезные привычки"

    def __str__(self):
        return f"{self.action} - {self.user}"
