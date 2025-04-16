from celery import shared_task
from django.utils import timezone
from .models import ScheduledReward, RewardLog, User


@shared_task
def process_scheduled_rewards():
    now = timezone.now()
    rewards = ScheduledReward.objects.filter(
        execute_at__lte=now,
        is_processed=False
    )

    for reward in rewards:
        try:
            user = reward.user
            user.coins += reward.amount
            user.save()

            RewardLog.objects.create(
                user=user,
                amount=reward.amount
            )

            reward.is_processed = True
            reward.save()
        except Exception as e:
            print(f"Error processing reward {reward.id}: {str(e)}")