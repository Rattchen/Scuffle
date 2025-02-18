from django.urls import path
from .views import IndexView, LeaderboardView, ClanListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clans', ClanListView.as_view(), name='clan_list'),
    path('leaderboard', LeaderboardView.as_view(), name='leaderboard')

]