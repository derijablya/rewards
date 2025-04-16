from celery import shared_task
from .models import ScheduledReward, RewardLog


@shared_task
def process_scheduled_reward(reward_id):
    try:
        reward = ScheduledReward.objects.get(id=reward_id)
        reward.user.coins += reward.amount
        reward.user.save()

        RewardLog.objects.create(user=reward.user, amount=reward.amount)
        reward.delete()
    except ScheduledReward.DoesNotExist:
        pass
