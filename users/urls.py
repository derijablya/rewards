from django.urls import path
from .views import RewardLogView, RequestRewardView

urlpatterns = [
    path('config/', RewardLogView.as_view(), name='config-list'),
    path('config/request/', RequestRewardView.as_view(), name='request-reward'),
]