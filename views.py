from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.db.models import F
from .models import Clan, ScuffleProfile

class IndexView(TemplateView):
    template_name = 'scuffle/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hi, welcome to Scuffle module!'
        return context

class ClanListView(ListView):
    # TODO: Most points user + points in total for each clan
    template_name = 'scuffle/clan_list.html'
    model = Clan
    context_object_name = "clans"

class ClanDetailView(DetailView):
    model = Clan
    template_name = 'scuffle/clan.html'

class LeaderboardView(TemplateView):
    template_name = 'scuffle/leaderboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clans = Clan.objects.all()
        context['clans'] = clans

        for clan in context['clans']:
            clan.leaderboard = clan.people.all().annotate(
                total_points = F('points')+F('nibbleProfile__points') #calculate manually since it's not a field but a @property
            ).order_by('-total_points')
        return context

class ScuffleProfileDetailView(DetailView):
    model = ScuffleProfile
    template_name = 'scuffle/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        activities = profile.activities.all()
        context["activities"] = activities
        return context

    def get_object(self):
        return get_object_or_404(ScuffleProfile, nibbleProfile__handle=self.kwargs["handle"])