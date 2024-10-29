from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(
        verbose_name="email", help_text="Введите свой email", unique=True
    )

    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="телеграм chat-id",
        help_text="введите телеграм chat-id",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
