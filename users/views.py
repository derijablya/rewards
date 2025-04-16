from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import RewardLog, ScheduledReward
from .serializers import UserProfileSerializer, RewardLogSerializer
from django.utils import timezone
from datetime import timedelta
from .tasks import process_scheduled_reward


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


class RewardLogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rewards = RewardLog.objects.filter(user=request.user).order_by('-given_at')
        serializer = RewardLogSerializer(rewards, many=True)
        return Response(serializer.data)


class RequestRewardView(APIView):
    def post(self, request):
        if RewardLog.objects.filter(
            user=request.user,
            given_at__date=timezone.now().date()
        ).exists():
            return Response(
                {"error": "You can request only one reward per day"},
                status=status.HTTP_400_BAD_REQUEST
            )

        execute_at = timezone.now() + timedelta(minutes=5)
        reward = ScheduledReward.objects.create(
            user=request.user,
            amount=10,
            execute_at=execute_at
        )

        process_scheduled_reward.apply_async(
            args=[reward.id],
            eta=execute_at
        )

        return Response(
            {"message": f"Reward will be given at {execute_at}"},
            status=status.HTTP_201_CREATED
        )