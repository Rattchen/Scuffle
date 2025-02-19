from django.db import models
from nibble.models import NibbleProfile

class Clan(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=5, default="🏠")
    description = models.TextField()

    def __str__(self):
        return self.name

class ScuffleProfile(models.Model):
    nibbleProfile = models.OneToOneField(NibbleProfile, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE, null=True, blank=True, related_name="people")

    @property
    def points_in_total(self):
        return (self.nibbleProfile.points + self.points)

    def __str__(self):
        return f"@{self.nibbleProfile.handle} ({self.nibbleProfile.user.username})"

class Season(models.Model):
    ordinal = models.IntegerField(unique=True)
    name = models.CharField(max_length=250, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    has_finished = models.BooleanField()

    def __str__(self):
        return f"Season {self.ordinal}: {self.name}"

class ClanSeasonRecord(models.Model):
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE, related_name="clan_records")
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="season_records")
    points_total = models.IntegerField()
    rank = models.PositiveIntegerField()
    out_of = models.PositiveIntegerField() # How many clans there were in given season

    def __str__(self):
        return f"{self.clan.name} during season {self.season.ordinal}: {self.rank}/{self.out_of}"

class Activity(models.Model):
    name = models.CharField(max_length=250)
    points = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(ScuffleProfile, on_delete=models.CASCADE, related_name="activities")

    def __str__(self):
        return f"{self.points} pts for {self.assigned_to.nibbleProfile.user.username}: {self.name}"
