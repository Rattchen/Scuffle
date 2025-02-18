from django.urls import path
from .views import IndexView, LeaderboardView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('leaderboard', LeaderboardView.as_view(), name='leaderboard')

]