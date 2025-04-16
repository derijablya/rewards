from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    coins = models.IntegerField(default=0)

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
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Scheduled reward for {self.user.username} at {self.execute_at}"