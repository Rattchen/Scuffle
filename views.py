from django.views.generic import TemplateView, ListView
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

