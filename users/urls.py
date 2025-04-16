from django.urls import path
from .views import RewardLogView, RequestRewardView

urlpatterns = [
    path('rewards/', RewardLogView.as_view(), name='rewards-list'),
    path('rewards/request/', RequestRewardView.as_view(), name='request-reward'),
]