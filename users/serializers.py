from rest_framework import serializers
from .models import User
from .models import RewardLog, ScheduledReward


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'coins')
        read_only_fields = ('coins',)

class RewardLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = ('id', 'amount', 'given_at')
        read_only_fields = fields


class ScheduledRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledReward
        fields = ('id', 'amount', 'execute_at')