from django.db import models
from django.contrib.auth.models import AbstractUser


class TgGroup(models.Model):
    title = models.CharField("Telegram Group Name", max_length=100)
    tutor = models.ForeignKey('user.User', models.CASCADE)

    class Meta:
        verbose_name = "Telegram Group"
        verbose_name_plural = "Telegram Groups"

    def __str__(self):
        return self.title


class User(AbstractUser):
    """Users can diffentiate by their status.
        has no status -> student,
        is_staff -> tutor,
        is_superuser -> developer.
    """
    group = models.ForeignKey('user.TgGroup', models.SET_NULL, null=True, related_name='students')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
