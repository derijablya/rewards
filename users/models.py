from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    coins = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.username


class RewardLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    given_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} coins at {self.given_at}"

class ScheduledReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    execute_at = models.DateTimeField()

    def __str__(self):
        return f"Scheduled reward for {self.user.username} at {self.execute_at}"