from django.urls import path
from .views import IndexView, LeaderboardView, ClanListView, ClanDetailView, ScuffleProfileDetailView

app_name = "scuffle"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clans', ClanListView.as_view(), name='clan_list'),
    path('clan/<int:pk>', ClanDetailView.as_view(), name='clan'),
    path('leaderboard', LeaderboardView.as_view(), name='leaderboard'),
    path('profile/<str:handle>', ScuffleProfileDetailView.as_view(), name='profile'),

]