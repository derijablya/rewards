from django.contrib import admin
from .models import User, ScheduledReward, RewardLog
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'coins')

@admin.register(RewardLog)
class RewardLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'given_at')

@admin.register(ScheduledReward)
class ScheduledRewardAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'execute_at')