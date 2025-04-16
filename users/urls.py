from django.urls import path
from .views import RewardLogView, RequestRewardView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("rewards/", RewardLogView.as_view(), name="reward-list"),
    path("rewards/request/", RequestRewardView.as_view(), name="request-reward"),
]
