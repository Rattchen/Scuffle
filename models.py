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
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def points_in_total(self):
        return (NibbleProfile.points + self.points)

    def __str__(self):
        return f"@{self.nibbleProfile.handle} ({self.nibbleProfile.user.username})"
