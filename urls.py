from django.urls import path
from .views import IndexView, LeaderboardView, ClanListView, ClanDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clans', ClanListView.as_view(), name='clan_list'),
    path('clan/<int:pk>', ClanDetailView.as_view(), name='clan'),
    path('leaderboard', LeaderboardView.as_view(), name='leaderboard')

]