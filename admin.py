from django.contrib import admin
from .models import ScuffleProfile, Clan, Season, ClanSeasonRecord, Activity


admin.site.register(ScuffleProfile)
admin.site.register(Clan)
admin.site.register(Season)
admin.site.register(ClanSeasonRecord)
admin.site.register(Activity)